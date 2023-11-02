def solution():
    # Calculate the number of apple trees in Hassan's orchard
    hassan_apple_trees = 1
    ahmed_apple_trees = 4 * hassan_apple_trees  # Ahmed has four times as many apple trees as Hassan
    hassan_orange_trees = 2
    ahmed_orange_trees = 8  # Ahmed has 8 orange trees

    # Calculate the total number of trees in each orchard
    hassan_total_trees = hassan_apple_trees + hassan_orange_trees
    ahmed_total_trees = ahmed_apple_trees + ahmed_orange_trees

    # Calculate the difference between the total number of trees in Ahmed's and Hassan's orchards
    difference = ahmed_total_trees - hassan_total_trees
    result = difference
    return result

print(solution())