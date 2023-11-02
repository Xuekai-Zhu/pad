def solution():
    """Josh has 85 marbles. There are three times as many blue marbles as red while the rest are yellow. If there are 14 red marbles, how many yellow marbles are there?"""
    # Define the number of red marbles
    red_marbles = 14

    # Calculate the number of blue marbles
    blue_marbles = 3 * red_marbles

    # Calculate the total number of red and blue marbles
    total_red_blue = red_marbles + blue_marbles

    # Calculate the number of yellow marbles
    yellow_marbles = 85 - total_red_blue

    # Display the number of yellow marbles
    result = yellow_marbles
    return result

print(solution())