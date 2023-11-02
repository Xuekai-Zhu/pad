def solution():
    """A four-layer pyramid is being built with each layer having three times as many sandstone blocks as the layer above it. The top layer is a single block. How many sandstone blocks are in the pyramid?"""
    top_layer = 1
    second_layer = top_layer * 3
    third_layer = second_layer * 3
    bottom_layer = third_layer * 3
    total_blocks = top_layer + second_layer + third_layer + bottom_layer
    result = total_blocks
    return result

print(solution())