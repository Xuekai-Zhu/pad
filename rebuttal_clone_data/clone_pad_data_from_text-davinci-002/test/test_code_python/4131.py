def solution():
    box_height = 4
    box_width = 6
    block_height = 4
    block_width = block_height
    box_area = box_height * box_width
    block_area = block_height * block_width
    uncoverd_area = box_area - block_area
    result = uncoverd_area
    return result

print(solution())