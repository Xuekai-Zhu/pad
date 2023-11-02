def solution():
    """Mary is trying to get Zoom set up for the first time. She spent 10 minutes downloading the Mac version, only to realize she needed the Windows version, which took three times as long to download. During her first call, the audio glitched twice for 4 minutes each time and the video glitched once for 6 minutes. She spent twice as long talking without glitches as with glitches. How much time did Mary spend downloading Zoom and talking total?"""
    mac_download_time = 10
    windows_download_time = 3 * mac_download_time
    total_download_time = mac_download_time + windows_download_time
    audio_glitch_time = 2 * 4
    video_glitch_time = 6
    total_glitch_time = audio_glitch_time + video_glitch_time
    total_talking_time_with_glitches = total_glitch_time
    total_talking_time_without_glitches = 2 * total_talking_time_with_glitches
    total_talking_time = total_talking_time_with_glitches + total_talking_time_without_glitches
    total_time = total_download_time + total_talking_time
    result = total_time
    return result

print(solution())