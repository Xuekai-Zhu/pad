def solution():
    """A wildlife team is monitoring the number of birds in a park. There are 3 blackbirds in each of the park’s 7 trees. There are also 13 magpies roaming around the park. How many birds are in the park in total?"""
    # Define the number of blackbirds per tree
    BLACKBIRDS_PER_TREE = 3

    # Define the number of trees in the park
    trees = 7

    # Calculate the total number of blackbirds in the park
    blackbirds = BLACKBIRDS_PER_TREE * trees

    # Add the number of magpies in the park
    total_birds = blackbirds + 13

    # Display the total number of birds in the park
    result = total_birds
    return result

print(solution())