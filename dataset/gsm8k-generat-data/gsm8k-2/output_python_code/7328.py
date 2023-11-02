def solution():
    """Tara has a shoebox that is 4 inches tall and 6 inches wide. She puts a square block inside that is 4 inches per side. How many square inches of the box are left uncovered?"""
    box_height = 4
    box_width = 6
    block_size = 4
    block_area = block_size ** 2
    box_area = box_height * box_width
    uncovered_area = box_area - block_area
    result = uncovered_area
    return result

print(solution())