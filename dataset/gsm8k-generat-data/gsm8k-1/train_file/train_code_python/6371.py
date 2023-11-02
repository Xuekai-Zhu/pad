def solution():
    """Mary is trying to get Zoom set up for the first time. She spent 10 minutes downloading the Mac version, only to realize she needed the Windows version, which took three times as long to download. During her first call, the audio glitched twice for 4 minutes each time and the video glitched once for 6 minutes. She spent twice as long talking without glitches as with glitches. How much time did Mary spend downloading Zoom and talking total?"""
    download_mac = 10
    download_windows = download_mac * 3
    audio_glitch_time = 4 * 2
    video_glitch_time = 6
    total_glitch_time = audio_glitch_time + video_glitch_time
    total_talk_time = total_glitch_time * 2
    total_download_time = download_mac + download_windows
    total_time = total_download_time + total_glitch_time + total_talk_time
    result = total_time
    return result

print(solution())