def solution():
    # Calculate the number of layers that are not limestone
    non_limestone_layers = 25 - 5  # there are 25 layers in total, and 5 of them are limestone

    # Calculate the number of sandstone layers
    sandstone_layers = non_limestone_layers // 2

    # Calculate the number of quartz layers
    quartz_layers = 4

    # Calculate the number of shale layers
    shale_layers = (non_limestone_layers - sandstone_layers - quartz_layers) // 2

    # Calculate the number of layers that are different kinds of rock
    different_rocks_layers = non_limestone_layers - sandstone_layers - quartz_layers - shale_layers

    # Calculate the number of kinds of rock that make up only one layer
    one_layer_kinds_of_rock = different_rocks_layers

    result = one_layer_kinds_of_rock
    return result

print(solution())