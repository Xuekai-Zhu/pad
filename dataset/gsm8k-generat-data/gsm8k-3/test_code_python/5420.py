def solution():
    """There are 19 marbles in a bowl, 5 of which are yellow. The remainder are split into blue marbles and red marbles in the ratio 3:4 respectively. How many more red marbles than yellow marbles are there?"""
    # Define the number of yellow marbles
    yellow_marbles = 5

    # Calculate the number of blue and red marbles
    total_blue_red = 19 - yellow_marbles
    blue_marbles = total_blue_red * (3/7)
    red_marbles = total_blue_red * (4/7)

    # Calculate the difference between the number of red and yellow marbles
    difference = red_marbles - yellow_marbles

    # Display the difference
    result = difference
    return result

print(solution())