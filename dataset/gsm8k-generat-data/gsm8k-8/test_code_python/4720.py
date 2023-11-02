def solution():
    # Define the number of yellow and green marbles
    yellow_marbles = 20
    green_marbles = yellow_marbles / 2

    # Calculate the number of red and blue marbles
    total_other_marbles = 60 - yellow_marbles - green_marbles
    other_marbles_each = total_other_marbles / 2
    blue_marbles = other_marbles_each

    # Calculate the odds of picking a blue marble
    total_blue_marbles = blue_marbles
    total_possible_marbles = 60
    odds_of_blue = (total_blue_marbles / total_possible_marbles) * 100
    result = odds_of_blue
    return result

print(solution())