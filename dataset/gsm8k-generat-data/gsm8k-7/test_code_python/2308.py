def solution():
    bandages_left = (2 * 2) + (3 * 2)  # Peggy used two bandages on each knee
    box_size = 2 * 12 - 8
    bandages_left = box_size - bandages_left
    result = bandages_left
    return result

print(solution())