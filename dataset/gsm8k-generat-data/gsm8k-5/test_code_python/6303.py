def solution():
    total_marbles = 63  
    dark_blue_marbles = total_marbles / 3  # At least one-third of the marbles are dark blue
    green_marbles = 4  # There are only 4 green marbles
    red_marbles = total_marbles - dark_blue_marbles - green_marbles  # The rest of the marbles are red

    result = red_marbles
    return result

print(solution())