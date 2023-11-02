def solution():
    """Mary is trying to get Zoom set up for the first time. She spent 10 minutes downloading the Mac version,
    only to realize she needed the Windows version, which took three times as long to download.
    During her first call, the audio glitched twice for 4 minutes each time and the video glitched once for 6 minutes.
    She spent twice as long talking without glitches as with glitches. How much time did Mary spend downloading Zoom
    and talking total?"""
    # Define the download times and glitch times
    MAC_DOWNLOAD_TIME = 10
    WINDOWS_DOWNLOAD_TIME = MAC_DOWNLOAD_TIME * 3
    AUDIO_GLITCH_TIME = 4 * 2
    VIDEO_GLITCH_TIME = 6

    # Calculate the total download time
    download_time = MAC_DOWNLOAD_TIME + WINDOWS_DOWNLOAD_TIME

    # Calculate the total time spent talking with and without glitches
    total_talk_time = (AUDIO_GLITCH_TIME + VIDEO_GLITCH_TIME) * 2
    talk_without_glitches = total_talk_time / 3
    talk_with_glitches = talk_without_glitches * 2
    total_talk_time = talk_with_glitches + talk_without_glitches

    # Calculate the total time Mary spent downloading and talking
    total_time = download_time + total_talk_time

    # Display the total time
    result = total_time
    return result

print(solution())