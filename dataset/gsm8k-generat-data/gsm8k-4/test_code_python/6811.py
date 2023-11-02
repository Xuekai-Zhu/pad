def solution():
    """There are 24 marbles in a jar. Half are blue. There are 6 red marbles. The rest of the marbles are orange. How many orange marbles are there?"""
    # Define the total number of marbles and the number of red marbles
    total_marbles = 24
    red_marbles = 6

    # Calculate the number of blue marbles
    blue_marbles = total_marbles / 2

    # Calculate the number of orange marbles
    orange_marbles = total_marbles - blue_marbles - red_marbles

    # return the result
    result = orange_marbles
    return result

print(solution())