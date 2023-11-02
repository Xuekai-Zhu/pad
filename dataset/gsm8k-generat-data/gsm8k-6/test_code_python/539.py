def solution():
    # Calculate the total number of trees chopped down in the year
    total_trees_chopped = 200 + 300  

    # Calculate the total number of trees the company needs to plant to replace the trees chopped down
    trees_to_plant = 3 * total_trees_chopped - total_trees_chopped  # for every tree chopped down, the company wants to plant three more
    result = trees_to_plant
    return result

print(solution())