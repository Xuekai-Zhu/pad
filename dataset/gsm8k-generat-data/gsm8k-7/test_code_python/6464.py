def solution():
    num_mahogany_trees_planted = 0
    num_narra_trees_planted = 0

    # Subtract the number of fallen trees
    num_mahogany_trees = 50
    num_narra_trees = 30
    num_fallen_trees = 5
    num_mahogany_fallen = num_narra_fallen + 1
    
    num_mahogany_trees -= num_mahogany_fallen
    num_narra_trees -= num_narra_fallen

    # Calculate the number of trees planted a month after the typhoon
    num_mahogany_planted = 3 * num_mahogany_fallen
    num_narra_planted = 2 * num_narra_fallen

    num_mahogany_trees_planted += num_mahogany_planted
    num_narra_trees_planted += num_narra_planted

    # Calculate the total number of trees now
    total_mahogany_trees = num_mahogany_trees + num_mahogany_trees_planted
    total_narra_trees = num_narra_trees + num_narra_trees_planted

    total_trees = total_mahogany_trees + total_narra_trees

    result = total_trees
    return result

print(solution())