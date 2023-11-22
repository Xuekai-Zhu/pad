def solution():
    
    # Define the initial number of trees
    initial_trees = 50

    # Define the number of trees planted and chops down each year
    planted_trees = 10
    chopped_trees = 2

    # Calculate the total number of trees planted
    total_planted = planted_trees * 10

    # Calculate the total number of trees chopped down
    total_chopped = chopped_trees * 10

    # Calculate the total number of trees remaining after 10 years
    remaining_trees = initial_trees - total_planted - total_chopped

    # Calculate the number of trees that die after 10 years
    die_trees = remaining_trees * 0.3

    # Calculate the final number of trees remaining
    final_trees = remaining_trees - die_trees

    # return the result
    result = final_trees
    return result

print(solution())