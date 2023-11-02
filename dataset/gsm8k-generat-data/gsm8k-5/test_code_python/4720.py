def solution():
    total_marbles = 60
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2  # Half as many as yellow marbles
    red_and_blue_marbles = total_marbles - yellow_marbles - green_marbles

    # Divide the remaining marbles equally between red and blue
    blue_marbles = red_and_blue_marbles / 2

    # Calculate the probability of picking a blue marble
    probability_blue = blue_marbles / total_marbles
    percentage_blue = probability_blue * 100
    result = percentage_blue
    return result

print(solution())