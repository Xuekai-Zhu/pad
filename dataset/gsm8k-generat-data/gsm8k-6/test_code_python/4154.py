def solution():
    layer_blocks = 1  # number of sandstone blocks in the top layer
    total_blocks = 0  # total number of sandstone blocks in the pyramid
    
    # Loop through each layer of the pyramid and calculate the number of blocks
    for i in range(4):
        total_blocks += layer_blocks  # add the current layer to the total
        layer_blocks *= 3  # calculate the number of blocks in the next layer (3 times the previous layer)
        
    result = total_blocks
    return result

print(solution())