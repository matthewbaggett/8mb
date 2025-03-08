#!/usr/bin/python3
import sys
import subprocess
import os
import argparse
import time
startTime = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='File to Crush', required=True)
parser.add_argument('-o', '--output', help='Output File', required=False)
parser.add_argument("-s", "--size", help="Target Size in MB", type=int, default=8)
parser.add_argument("-t", "--tolerance", help="Tolerance", type=int,default=10)
args = parser.parse_args()

def get_duration(fileInput):

    return float(
        subprocess.check_output([
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            fileInput
        ])[:-1]
    )

def transcode(fileInput, fileOutput, bitrate):
    command = [
        'ffmpeg',
            '-y',
            '-hide_banner',
            '-loglevel', 'error',
            '-i', fileInput,
            '-b', str(bitrate) + '',
            '-cpu-used', str(os.cpu_count()),
            '-c:a',
            'copy',
            fileOutput
      ]
    #print(command)
    proc = subprocess.run(
                command,
                capture_output=True,
                # avoid having to explicitly encode
                text=True
    )
    #print(proc.stdout)

# Tolerance below 8mb
tolerance = args.tolerance
fileInput = args.file
if args.output:
    fileOutput = args.output
else:
    fileOutput = fileInput[:fileInput.rindex('.')] + '.crushed' + fileInput[fileInput.rindex('.'):]
targetSizeKilobytes = args.size * 1024
targetSizeBytes = targetSizeKilobytes * 1024
durationSeconds = get_duration(fileInput)
bitrate = round( targetSizeBytes / durationSeconds)
beforeSizeBytes = os.stat(fileInput).st_size

print("Crushing", fileInput, "to", targetSizeKilobytes, "KB with tolerance", tolerance, "%")

factor = 0
attempt = 0
while (factor > 1.0 + (tolerance/100)) or (factor < 1):
    attempt = attempt + 1
    bitrate = round(bitrate * (factor or 1))
    print("Attempt", attempt, ": Transcoding", fileInput, "at bitrate", bitrate)

    transcode(fileInput, fileOutput, bitrate)
    afterSizeBytes = os.stat(fileOutput).st_size
    percentOfTarget = (100/targetSizeBytes)*afterSizeBytes
    factor = 100/percentOfTarget
    print(
        "Attempt",attempt,
        ": Original size:", '{:.2f}'.format(beforeSizeBytes/1024/1024), "MB",
        "New size:", '{:.2f}'.format(afterSizeBytes/1024/1024), "MB",
        "Percentage of target:", '{:.0f}'.format(percentOfTarget),
        "and bitrate", bitrate
    )

print("Completed in", attempt, "attempts over", round(time.time() - startTime, 2), "seconds")
print(" > Exported as", fileOutput)
