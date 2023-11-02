def solution():
    total_trees = 4000
    spruce_percentage = 0.1
    pine_percentage = 0.13
    oak_percentage = (1 - spruce_percentage - pine_percentage) / 2

    # Calculate the number of spruce trees
    num_spruces = total_trees * spruce_percentage

    # Calculate the number of pine trees
    num_pines = total_trees * pine_percentage

    # Calculate the number of oak trees
    num_oaks = (num_spruces + num_pines) / 2

    # Calculate the number of birch trees
    num_birches = total_trees - (num_spruces + num_pines + num_oaks)
    result = num_birches
    return result

print(solution())