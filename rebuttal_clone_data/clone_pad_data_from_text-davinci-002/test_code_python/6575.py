def solution():
    bed_height = 2
    bed_width = 2
    bed_length = 8
    side_width = 1
    plank_length = 8
    boards_needed = ((bed_length * 2) + (bed_width * 2) - 4) / plank_length
    result = boards_needed
    return result

print(solution())