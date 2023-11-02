def solution():
    ahmed_orange_trees = 8
    hassan_apple_trees = 1
    hassan_orange_trees = 2

    # Calculate the number of apple trees in Ahmed's orchard
    ahmed_apple_trees = hassan_apple_trees * 4

    # Calculate the total number of trees in Ahmed's orchard
    ahmed_total_trees = ahmed_orange_trees + ahmed_apple_trees

    # Calculate the total number of trees in Hassan's orchard
    hassan_total_trees = hassan_orange_trees + hassan_apple_trees

    # Calculate the difference in the number of trees between Ahmed and Hassan's orchards
    diff_trees = ahmed_total_trees - hassan_total_trees
    result = diff_trees
    return result

print(solution())