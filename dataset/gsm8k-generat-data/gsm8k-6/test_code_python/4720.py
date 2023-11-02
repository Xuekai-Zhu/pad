def solution():
    # Calculate the number of green marbles
    num_green = 20 / 2  # half as many as yellow marbles

    # Calculate the number of red and blue marbles
    num_red_blue = 60 - 20 - num_green  # remaining marbles

    # Calculate the odds of picking a blue marble
    odds_blue = (num_red_blue / 2) / 60  # divided equally between red and blue, total marbles = 60
    odds_blue_percent = odds_blue * 100

    result = odds_blue_percent
    return result

print(solution())