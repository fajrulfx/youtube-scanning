# youtube-screening
Simple code for bulk scanning of youtube videos

# Background
I have to scan more than 1000 youtube videos to find which video that mentions specific keyword inside the content.

# Method
- Using `youtube-dl` package to download the subtitle (vtt file) of the video
- Using `re.search` package to find which substitle file contains specified keyword
- Write the result in txt output file

# Notes
The link of youtube videos that will be scanned need to be listed manually and saved in a txt file. I haven't had time to create a script to automatically search for YouTube video links. This is a rush project :D
