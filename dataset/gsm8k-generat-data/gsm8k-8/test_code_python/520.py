def solution():
    # Define the number of limestone layers
    limestone_layers = 5

    # Calculate the number of layers that are not limestone
    non_limestone_layers = 25 - limestone_layers

    # Calculate the number of sandstone layers
    sandstone_layers = non_limestone_layers / 2

    # Calculate the number of layers that are not limestone or sandstone
    non_limestone_sandstone_layers = non_limestone_layers - sandstone_layers

    # Calculate the number of quartz layers
    quartz_layers = 4

    # Calculate the number of shale layers
    shale_layers = non_limestone_sandstone_layers / 2

    # Calculate the number of layers that are not limestone, sandstone, quartz, or shale
    other_layers = non_limestone_sandstone_layers - shale_layers

    # Calculate the number of kinds of rock that make up only one layer
    one_layer_kinds = other_layers

    result = one_layer_kinds
    return result

print(solution())