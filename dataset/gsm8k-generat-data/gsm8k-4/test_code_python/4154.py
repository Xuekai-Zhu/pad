def solution():
    """A four-layer pyramid is being built with each layer having three times as many sandstone blocks as the layer above it.
    The top layer is a single block. How many sandstone blocks are in the pyramid?"""
    # Define the number of layers in the pyramid
    num_layers = 4

    # Define the initial number of blocks in the top layer
    top_layer = 1

    # Define the total number of blocks as the top layer
    total_blocks = top_layer

    # Loop through the remaining layers and calculate the number of blocks in each layer
    for i in range(1, num_layers):
        # Calculate the number of blocks in the current layer as three times the number in the layer above it
        current_layer = 3 * top_layer

        # Add the current layer to the total number of blocks
        total_blocks += current_layer

        # Set the current layer as the new top layer for the next iteration
        top_layer = current_layer

    # return the result
    result = total_blocks
    return result

print(solution())