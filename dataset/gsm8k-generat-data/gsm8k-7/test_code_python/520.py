def solution():
    total_layers = 25
    limestone_layers = 5

    # Calculate the number of non-limestone layers
    non_limestone_layers = total_layers - limestone_layers

    # Calculate the number of sandstone layers (half of non-limestone layers)
    sandstone_layers = non_limestone_layers / 2

    # Calculate the number of remaining layers after sandstone and limestone
    remaining_layers = non_limestone_layers - sandstone_layers

    # Calculate the number of quartz layers
    quartz_layers = 4

    # Calculate the number of shale layers (half of remaining layers)
    shale_layers = remaining_layers / 2

    # Calculate the number of layers that are not limestone, sandstone, quartz, or shale
    other_layers = total_layers - limestone_layers - sandstone_layers - quartz_layers - shale_layers

    # Calculate the number of kinds of rock that make up only one layer
    single_layer_rocks = other_layers

    result = single_layer_rocks
    return result

print(solution())