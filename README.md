# 8mb
8MB video compression bash script for ffmpeg. 

I refuse to pay for Discord Nitro. Stop giving them money. They've raised [$0.9945 Bn of Venture Capital](https://www.crunchbase.com/organization/discord/company_financials). They don't need your money.

New, iterative process usage:
```
matthewbaggett@exploding-bolts:~$ 8mb.py ~/Downloads/chooch.mp4
Attempt 1 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 52667
Attempt 1 : Original size: 48.30 MB New size: 3.59 MB Percentage of target: 45 and bitrate 52667
Attempt 2 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 117441
Attempt 2 : Original size: 48.30 MB New size: 4.80 MB Percentage of target: 60 and bitrate 117441
Attempt 3 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 195825
Attempt 3 : Original size: 48.30 MB New size: 6.28 MB Percentage of target: 78 and bitrate 195825
Attempt 4 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 249600
Attempt 4 : Original size: 48.30 MB New size: 7.30 MB Percentage of target: 91 and bitrate 249600
Completed in 4 attempts.
```

Now with ~~gusto~~ docker:
```
matthewbaggett@exploding-bolts:~$ docker run -v ~/Downloads:/vidja matthewbaggett/8mb /vidja/chooch.mp4
Attempt 1 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 52667
Attempt 1 : Original size: 48.30 MB New size: 3.59 MB Percentage of target: 45 and bitrate 52667
Attempt 2 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 117441
Attempt 2 : Original size: 48.30 MB New size: 4.80 MB Percentage of target: 60 and bitrate 117441
Attempt 3 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 195825
Attempt 3 : Original size: 48.30 MB New size: 6.28 MB Percentage of target: 78 and bitrate 195825
Attempt 4 : Transcoding /home/geusebio/Downloads/chooch.mp4 at bitrate 249600
Attempt 4 : Original size: 48.30 MB New size: 7.30 MB Percentage of target: 91 and bitrate 249600
Completed in 4 attempts.
```

Old Usage:
```
matthewbaggett@bidness:~$ 8mb Downloads/video_2021-05-04_04-50-36.mp4
Shrinking Downloads/video_2021-05-04_04-50-36.mp4 to 8192KB. Bitrate: 1420k
Rebuilt file as Downloads/video_2021-05-04_04-50-36.mp4.shrunk.mp4, shrank to 14% of original size
```
