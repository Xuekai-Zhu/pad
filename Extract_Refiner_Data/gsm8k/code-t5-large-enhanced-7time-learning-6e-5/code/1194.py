def solution():
    
    # Define the number of trees planted on the first day
    white_oak_trees = 20
    lodgepole_pine_trees = 2 * white_oak_trees

    # Define the number of trees planted on the second day
    white_oak_trees += 10
    lodgepole_pine_trees += (1/4 * white_oak_trees)

    # Calculate the total number of trees planted
    total_trees = white_oak_trees + lodgepole_pine_trees

    # Display the total number of trees planted
    result = total_trees
    return result

print(solution())