from youtube import Video

video_url = ["3AtDnEC4zak", "3AtDnEC4zak"]

for vdo in video_url:
        v = Video(f"https://youtu.be/{vdo}").streams
        v.ffhigh.download() # ffhigh will download stream with highest quality

