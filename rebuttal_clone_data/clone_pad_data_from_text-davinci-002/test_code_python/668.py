def solution():
    box_height = 8
    box_width = 10
    box_length = 12
    block_height = 3
    block_width = 2
    block_length = 4
    total_blocks = ((box_height / block_height) * (box_width / block_width) * (box_length / block_length))
    result = total_blocks
    return result

print(solution())