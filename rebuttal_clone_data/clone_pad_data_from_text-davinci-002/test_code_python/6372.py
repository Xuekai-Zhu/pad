def solution():
    time_downloading_mac = 10
    time_downloading_windows = time_downloading_mac * 3
    time_with_glitches = 4 + 4 + 6
    time_without_glitches = 2 * time_with_glitches
    total_time = time_downloading_windows + time_with_glitches + time_without_glitches
    result = total_time
    return result

print(solution())