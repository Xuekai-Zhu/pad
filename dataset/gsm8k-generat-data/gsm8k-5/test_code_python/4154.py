def solution():
    top_layer = 1  # The top layer is a single block
    layer2 = 3 * top_layer  # The second layer has three times as many blocks as the layer above it
    layer3 = 3 * layer2  # The third layer has three times as many blocks as the layer above it
    layer4 = 3 * layer3  # The fourth layer has three times as many blocks as the layer above it

    # Calculate the total number of sandstone blocks in the pyramid
    total_blocks = top_layer + layer2 + layer3 + layer4
    result = total_blocks
    return result

print(solution())