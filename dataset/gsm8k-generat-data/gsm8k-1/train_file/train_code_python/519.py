def solution():
    """There are 25 different layers of rock in a canyon’s strata. Five of the layers are limestone. Half of the rest are sandstone. Four of the remaining are quartz. Half of the rest are shale. The rest are all different kinds of rock. How many kinds of rock make up only one layer in the canyon’s strata?"""
    limestone = 5
    remaining_layers = 25 - limestone
    sandstone = remaining_layers / 2
    remaining_layers -= sandstone
    quartz = 4
    remaining_layers -= quartz
    shale = remaining_layers / 2
    one_layer = 1
    kinds_of_rock = remaining_layers - one_layer
    result = kinds_of_rock
    return result

print(solution())