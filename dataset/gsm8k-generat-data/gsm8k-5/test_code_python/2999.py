def solution():
    total_marbles = 50  # George collected 50 marbles in total
    white_marbles = total_marbles / 2  # Half of the marbles are white
    yellow_marbles = 12  # 12 marbles are yellow

    # Calculate the number of green marbles
    green_marbles = yellow_marbles / 2  # There are 50% fewer green marbles than yellow marbles

    # The sum of white, yellow, green, and red marbles is equal to the total number of marbles
    # Solving for red marbles:
    red_marbles = total_marbles - (white_marbles + yellow_marbles + green_marbles)
    result = red_marbles
    return result

print(solution())