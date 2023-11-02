def solution():
    
    top_layer = 1
    second_layer = top_layer * 3
    third_layer = second_layer * 3
    bottom_layer = third_layer * 3
    total_blocks = top_layer + second_layer + third_layer + bottom_layer
    result = total_blocks
    return result

print(solution())