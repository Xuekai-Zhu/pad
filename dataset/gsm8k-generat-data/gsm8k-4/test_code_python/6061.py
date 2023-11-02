def solution():
    """Josh has 85 marbles. There are three times as many blue marbles as red while the rest are yellow. If there are 14 red marbles, how many yellow marbles are there?"""
    # Define the total number of marbles and the number of red marbles
    total_marbles = 85
    red_marbles = 14

    # Calculate the number of blue marbles
    blue_marbles = red_marbles * 3

    # Calculate the number of yellow marbles
    yellow_marbles = total_marbles - red_marbles - blue_marbles

    # Return the result
    result = yellow_marbles
    return result

print(solution())