# yt-dlp - livechat json to srt converter
Converts the *.live_chat.json file into a .srt subtitle file

The original code can be found [here](https://gist.github.com/kylemsguy/dbdc3af9a88ff0079d40d8d39059b2b5)

# Requirements
* You have to install python3 and yt-dlp first to use it.

# Usage 
* At first download the the *.live_chat.json file with yt-dlp and rename it to "live_chat.json" after that.

EXAMPLE:
```
yt-dlp --write-subs --sub-lang live_chat https://www.youtube.com/watch?v=XXXXXXXXXXX
```
* Then download the "json2srt.py" python script and run it with
```
python3 json2srt.py
```
* After that you should get a converted "subtitle.srt" file.
* Now you can add the subtitle.srt file to your e.g. VLC player to watch the video with live chats as subtitles.

# Donation
monero: 8ApnFxFz4e399oQerTDwx1db7H9YnP3Rehb22PShSX6jP1To6GeXHweXY4KdXsttP3Gy7JMZ92TXmjQAWupCTjXNAG9cmFt

If you don't have $XMR you can swap your coins with [cakewallet](https://cakewallet.com)
