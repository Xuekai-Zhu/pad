def solution():
    """Mary is trying to get Zoom set up for the first time. She spent 10 minutes downloading the Mac version, only to realize she needed the Windows version, which took three times as long to download. During her first call, the audio glitched twice for 4 minutes each time and the video glitched once for 6 minutes. She spent twice as long talking without glitches as with glitches. How much time did Mary spend downloading Zoom and talking total?"""
    # Define the time spent downloading the Mac version and the time spent downloading the Windows version
    download_mac = 10
    download_windows = download_mac * 3

    # Define the total time spent on glitches during the call
    audio_glitch_time = 4 * 2
    video_glitch_time = 6
    total_glitch_time = audio_glitch_time + video_glitch_time

    # Define the ratio of time spent talking without glitches to time spent talking with glitches
    talk_ratio = 2

    # Calculate the time spent talking with glitches
    talk_with_glitches = total_glitch_time * (1 / (1 + talk_ratio))

    # Calculate the time spent talking without glitches
    talk_without_glitches = talk_with_glitches * talk_ratio

    # Calculate the total time spent downloading and talking
    total_time = download_mac + download_windows + total_glitch_time + talk_with_glitches + talk_without_glitches

    result = total_time
    return result

print(solution())