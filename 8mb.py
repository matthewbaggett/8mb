#!/usr/bin/python3
import sys
import subprocess
import os

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
tolerance = 10
fileInput = sys.argv[1]
fileOutput = fileInput + ".crushed.mp4"
targetSizeKilobytes = 8192
targetSizeBytes = targetSizeKilobytes * 1024
durationSeconds = get_duration(sys.argv[1])
bitrate = round( targetSizeBytes / durationSeconds)
beforeSizeBytes = os.stat(fileInput).st_size

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
print("Completed in", attempt, "attempts.")
