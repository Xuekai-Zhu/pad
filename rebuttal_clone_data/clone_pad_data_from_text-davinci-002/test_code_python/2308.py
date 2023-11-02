def solution():
    total_bandages_needed = 2 + 3
    bandages_in_box = 2 * 12 - 8
    bandages_left = bandages_in_box - total_bandages_needed
    result = bandages_left
    return result

print(solution())