def solution():
    mac_download_time = 10
    windows_download_time = mac_download_time * 3
    audio_glitch_time = 4 * 2  # 2 glitches for 4 minutes each
    video_glitch_time = 6
    talk_time_with_glitches = (audio_glitch_time + video_glitch_time)
    talk_time_without_glitches = talk_time_with_glitches * 2
    total_time = mac_download_time + windows_download_time + talk_time_with_glitches + talk_time_without_glitches
    result = total_time
    return result

print(solution())