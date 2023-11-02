def solution():
    """There are 25 different layers of rock in a canyon’s strata. Five of the layers are limestone. Half of the rest are sandstone. Four of the remaining are quartz.
    Half of the rest are shale. The rest are all different kinds of rock. How many kinds of rock make up only one layer in the canyon’s strata?"""
    
    # Number of limestone layers
    num_limestone = 5
    
    # Number of non-limestone layers
    num_non_limestone = 25 - num_limestone
    
    # Number of sandstone layers
    num_sandstone = num_non_limestone // 2
    
    # Number of non-sandstone layers
    num_non_sandstone = num_non_limestone - num_sandstone
    
    # Number of quartz layers
    num_quartz = 4
    
    # Number of non-quartz layers
    num_non_quartz = num_non_sandstone - num_quartz
    
    # Number of shale layers
    num_shale = num_non_quartz // 2
    
    # Number of non-shale layers
    num_one_layer = num_non_quartz - num_shale
    
    # Display the number of kinds of rock that make up only one layer
    result = num_one_layer
    return result

print(solution())