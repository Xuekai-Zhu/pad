def solution():
    # Define the number of blocks in the top layer
    top_layer = 1

    # Calculate the number of blocks in each layer below it
    layer2 = 3 * top_layer
    layer3 = 3 * layer2
    layer4 = 3 * layer3

    # Calculate the total number of sandstone blocks in the pyramid
    total_blocks = top_layer + layer2 + layer3 + layer4
    result = total_blocks
    return result

print(solution())