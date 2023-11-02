def solution():
    """Tara has a shoebox that is 4 inches tall and 6 inches wide. She puts a square block inside that is 4 inches per side. How many square inches of the box are left uncovered?"""
    box_height = 4
    box_width = 6
    block_side = 4
    block_area = block_side ** 2
    remaining_area = box_height * box_width - block_area
    result = remaining_area
    return result

print(solution())