def solution():
    """George collected 50 marbles in white, yellow, green, and red. Half of them are white, and 12 are yellow. There are 50% fewer green balls than yellow balls. How many marbles are red?"""
    # Define the total number of marbles
    total_marbles = 50

    # Calculate the number of white marbles
    white_marbles = total_marbles / 2

    # Calculate the number of yellow marbles
    yellow_marbles = 12

    # Calculate the number of green marbles
    green_marbles = yellow_marbles * 0.5

    # Calculate the number of red marbles
    red_marbles = total_marbles - white_marbles - yellow_marbles - green_marbles

    # Return the result
    result = red_marbles
    return result

print(solution())