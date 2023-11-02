def solution():
    
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