def solution():
    
    # Define the number of White Oak trees planted on the first day
    white_oak_1 = 20

    # Calculate the number of Lodgepole Pine trees planted on the first day
    lodgepole_pine_1 = 2 * white_oak_1

    # Calculate the number of White Oak trees planted on the second day
    white_oak_2 = white_oak_1 + 10

    # Calculate the number of Lodgepole Pine trees planted on the second day
    lodgepole_pine_2 = white_oak_2 * (1 + 1/4)

    # Calculate the total number of trees planted
    total_trees = white_oak_1 + lodgepole_pine_1 + lodgepole_pine_2

    # Display the total number of trees planted
    result = total_trees
    return result

print(solution())