    from youtube import Video
    v = Video("https://www.youtube.com/watch?v=3AtDnEC4zak")
    v.title
"Charlie Puth - We Don't Talk Anymore (feat. Selena Gomez) [Official Video]"
    v.length
231
    v.views
2550001850
    v.streams
[<Class Stream: itag="18" qualityLabel="360p" fps="24" mime="video/mp4" type="both" format="mp4" codecs="avc1.42001E,+mp4a.40.2">, 
<Class Stream: itag="133" qualityLabel="240p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.4d4015">, 
<Class Stream: itag="134" qualityLabel="360p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.4d401e">, 
<Class Stream: itag="135" qualityLabel="480p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.4d401e">, 
<Class Stream: itag="136" qualityLabel="720p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.4d401f">, 
<Class Stream: itag="137" qualityLabel="1080p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.640028">, 
<Class Stream: itag="160" qualityLabel="144p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="avc1.4d400c">, 
<Class Stream: itag="242" qualityLabel="240p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="243" qualityLabel="360p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="244" qualityLabel="480p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="247" qualityLabel="720p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="248" qualityLabel="1080p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="249" bitrate="59056" mime="audio/webm" type="audio" format="webm" codecs="opus">, 
<Class Stream: itag="250" bitrate="76035" mime="audio/webm" type="audio" format="webm" codecs="opus">, 
<Class Stream: itag="251" bitrate="143852" mime="audio/webm" type="audio" format="webm" codecs="opus">, 
<Class Stream: itag="278" qualityLabel="144p" fps="24" mime="video/webm" type="video" format="webm" codecs="vp9">, 
<Class Stream: itag="394" qualityLabel="144p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.00M.08">, 
<Class Stream: itag="395" qualityLabel="240p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.00M.08">, 
<Class Stream: itag="396" qualityLabel="360p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.01M.08">, 
<Class Stream: itag="397" qualityLabel="480p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.04M.08">, 
<Class Stream: itag="398" qualityLabel="720p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.05M.08">, 
<Class Stream: itag="399" qualityLabel="1080p" fps="24" mime="video/mp4" type="video" format="mp4" codecs="av01.0.08M.08">]
    type(v.streams)
<class 'youtube.Stream.Queue'>
    v.thumbnail
'https://i.ytimg.com/vi/3AtDnEC4zak/maxresdefault.jpg'
    v.get_dict
[{'itag': 18, 'mimeType': 'video/mp4', 'bitrate': 395026, 'width': 640, 'height': 360, 'lastModified': '1580859977121104', 'contentLength': '11378647', 'quality': 'medium', 'fps': 24, 'qualityLabel': '360p', 'projectionType': 'RECTANGULAR', 'averageBitrate': 394913, 'audioQuality': 'AUDIO_QUALITY_LOW', 'approxDurationMs': '230504', 'audioSampleRate': '44100', 'audioChannels': 2, 'type': 'both', 'format': 'mp4', 'codecs': 'avc1.42001E,+mp4a.40.2', 's': 'mAq0QJ8wRQIgRe0DKBgGi4uiqHOk6dmrhwQKtFCcrhCKAvNHps-hzk0CIQDDW_HSmfLlD3-4G5x3XtamqDtAWRVkjYYGv_qFYUY4Ow====', 'sp': 'sig', 'url': 'https://r7---sn-ci5gup-civl.googlevideo.com/videoplayback?expire=1606933954&ei=YonHX_XTBIKqvQSXv4-QDg ...........

