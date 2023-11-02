def solution():
    # Calculate the total number of marbles in the jar
    green_marbles = 27
    yellow_marbles = 14
    blue_marbles = (1/2) * (green_marbles + yellow_marbles)  # half of the marbles are blue
    red_marbles = (1/4) * (green_marbles + yellow_marbles)  # a quarter of the marbles are red
    total_marbles = green_marbles + yellow_marbles + blue_marbles + red_marbles
    result = total_marbles
    return result

print(solution())