def solution():
    
    # Define the number of blue birds in each tree
    BLUE_BIRDS_PER_TREE = 7

    # Define the number of trees
    trees = [3, 2, 2, 3]

    # Calculate the total number of blue birds
    total_blue_birds = sum(trees) * BLUE_BIRDS_PER_TREE

    # Display the total number of blue birds
    result = total_blue_birds
    return result

print(solution())