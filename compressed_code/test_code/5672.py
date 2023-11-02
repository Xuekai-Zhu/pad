def solution():
    
    box_height = 4
    box_width = 6
    block_size = 4
    block_area = block_size ** 2
    box_area = box_height * box_width
    uncovered_area = box_area - block_area
    result = uncovered_area
    return result

print(solution())