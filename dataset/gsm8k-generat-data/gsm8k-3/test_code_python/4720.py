def solution():
    """Cara has 60 marbles in a bag. 20 of them are yellow, half as many are green, and the remaining marbles are equally divided between red and blue. If Cara picks a marble at random, what are the odds it's blue (expressed as a percentage)?"""
    # Define the number of yellow marbles
    yellow_marbles = 20

    # Calculate the number of green marbles
    green_marbles = yellow_marbles / 2

    # Calculate the number of red and blue marbles combined
    red_blue_marbles = 60 - yellow_marbles - green_marbles

    # Calculate the number of blue marbles
    blue_marbles = red_blue_marbles / 2

    # Calculate the probability of picking a blue marble
    probability = blue_marbles / 60 * 100

    # Display the probability as a percentage
    result = probability
    return result

print(solution())