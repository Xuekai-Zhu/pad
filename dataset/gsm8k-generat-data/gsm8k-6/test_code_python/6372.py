def solution():
    # Calculate the total time Mary spent downloading Zoom and on her call
    download_time = 10 + 3*10  # the Windows version took three times as long as the Mac version to download
    total_glitch_time = 2*4 + 6  # audio glitched twice for 4 minutes each time and video glitched once for 6 minutes
    talk_time_with_glitches = total_glitch_time  # Mary spent twice as long talking with glitches as without
    talk_time_without_glitches = talk_time_with_glitches / 2  # calculate the time Mary spent talking without glitches
    total_talk_time = talk_time_with_glitches + talk_time_without_glitches  # calculate the total time Mary spent talking
    total_time = download_time + total_talk_time  # calculate the total time Mary spent downloading Zoom and talking
    result = total_time
    return result

print(solution())