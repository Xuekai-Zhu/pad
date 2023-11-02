def solution():
    # Time spent downloading Zoom
    mac_download_time = 10  # 10 minutes to download the Mac version
    windows_download_time = 3 * mac_download_time  # Windows version took 3 times as long
    total_download_time = mac_download_time + windows_download_time

    # Time spent on call
    total_call_time = 2 * total_call_time_with_glitches  # Twice as long without glitches
    total_call_time_with_glitches = 2 * 4 + 6  # Audio glitched twice for 4 minutes each and video glitched for 6 minutes

    # Total time spent
    total_time = total_download_time + total_call_time
    result = total_time
    return result

print(solution())