def solution():
    num_blocks_top_layer = 1
    num_blocks_second_layer = num_blocks_top_layer * 3
    num_blocks_third_layer = num_blocks_second_layer * 3
    num_blocks_bottom_layer = num_blocks_third_layer * 3

    total_num_blocks = num_blocks_top_layer + num_blocks_second_layer + num_blocks_third_layer + num_blocks_bottom_layer

    result = total_num_blocks
    return result

print(solution())