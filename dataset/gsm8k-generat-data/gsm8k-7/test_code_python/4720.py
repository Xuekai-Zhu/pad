def solution():
    total_marbles = 60
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2
    red_blue_marbles = total_marbles - yellow_marbles - green_marbles

    # Calculate the number of blue marbles
    num_blue_marbles = red_blue_marbles / 2

    # Calculate the probability of picking a blue marble
    probability_blue = num_blue_marbles / total_marbles

    # Convert the probability to a percentage
    percentage_blue = probability_blue * 100

    result = percentage_blue
    return result

print(solution())