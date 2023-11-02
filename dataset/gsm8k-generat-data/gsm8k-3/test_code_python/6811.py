def solution():
    """There are 24 marbles in a jar. Half are blue. There are 6 red marbles. The rest of the marbles are orange. How many orange marbles are there?"""
    # Calculate the number of blue marbles
    blue_marbles = 24 // 2

    # Calculate the number of orange marbles
    orange_marbles = 24 - blue_marbles - 6

    # Display the number of orange marbles
    result = orange_marbles
    return result

print(solution())