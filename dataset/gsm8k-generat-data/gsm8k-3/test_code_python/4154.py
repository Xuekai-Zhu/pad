def solution():
    """A four-layer pyramid is being built with each layer having three times as many sandstone blocks as the layer above it. The top layer is a single block. How many sandstone blocks are in the pyramid?"""
    # Define the number of blocks in the top layer
    top_layer_blocks = 1

    # Calculate the number of blocks in each layer
    layer2_blocks = top_layer_blocks * 3
    layer3_blocks = layer2_blocks * 3
    layer4_blocks = layer3_blocks * 3

    # Calculate the total number of blocks in the pyramid
    total_blocks = top_layer_blocks + layer2_blocks + layer3_blocks + layer4_blocks

    # Display the total number of blocks
    result = total_blocks
    return result

print(solution())