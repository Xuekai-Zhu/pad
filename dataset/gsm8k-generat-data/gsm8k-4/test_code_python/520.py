def solution():
    """There are 25 different layers of rock in a canyon’s strata. Five of the layers are limestone. Half of the rest are sandstone. Four of the remaining are quartz. Half of the rest are shale. The rest are all different kinds of rock. How many kinds of rock make up only one layer in the canyon’s strata?"""
    # Define the initial number of different layers
    layers = 25

    # Number of limestone layers
    limestone_layers = 5

    # Remove the limestone layers from the total layers
    remaining_layers = layers - limestone_layers

    # Number of sandstone layers
    sandstone_layers = remaining_layers // 2

    # Remove the sandstone layers from the remaining layers
    remaining_layers = remaining_layers - sandstone_layers

    # Number of quartz layers
    quartz_layers = 4

    # Remove the quartz layers from the remaining layers
    remaining_layers = remaining_layers - quartz_layers

    # Number of shale layers
    shale_layers = remaining_layers // 2

    # Remove the shale layers from the remaining layers
    remaining_layers = remaining_layers - shale_layers

    # The remaining layers are all different kinds of rock
    result = remaining_layers
    return result

print(solution())