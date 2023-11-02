def solution():
    
    # Define the initial number of trees
    initial_trees = 50

    # Define the number of trees planted and chops down each year
    planted_trees = 10
    down_trees = 2

    # Calculate the number of trees remaining after 10 years
    remaining_trees = initial_trees - (planted_trees * 10) + (down_trees * 10)

    # Calculate the number of trees that die
    die_trees = 0.3 * remaining_trees

    # Calculate the final number of trees
    final_trees = remaining_trees - die_trees

    # Display the final number of trees
    result = final_trees
    return result

print(solution())