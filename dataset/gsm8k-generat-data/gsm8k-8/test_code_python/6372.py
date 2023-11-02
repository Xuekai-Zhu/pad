def solution():
    # Calculate the time spent downloading the Windows version
    windows_download_time = 10 * 3

    # Calculate the total time spent downloading
    total_download_time = 10 + windows_download_time

    # Calculate the total time spent with glitches
    glitches_time = 4 + 4 + 6

    # Calculate the time spent without glitches
    non_glitches_time = glitches_time * 2

    # Calculate the total talk time
    total_talk_time = glitches_time + non_glitches_time

    # Calculate the total time spent
    total_time = total_download_time + total_talk_time
    result = total_time
    return result

print(solution())