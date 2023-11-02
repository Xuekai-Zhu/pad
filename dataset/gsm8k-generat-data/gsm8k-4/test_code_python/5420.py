def solution():
    """There are 19 marbles in a bowl, 5 of which are yellow. The remainder are split into blue marbles and red marbles in the ratio 3:4 respectively. How many more red marbles than yellow marbles are there?"""
    # Define the total number of marbles and the number of yellow marbles
    total_marbles = 19
    yellow_marbles = 5

    # Calculate the number of blue marbles and red marbles
    blue_marbles = total_marbles - yellow_marbles
    red_marbles = (4/7) * blue_marbles

    # Calculate the difference between the number of red and yellow marbles
    difference = red_marbles - yellow_marbles

    # return the result
    result = difference
    return result

print(solution())