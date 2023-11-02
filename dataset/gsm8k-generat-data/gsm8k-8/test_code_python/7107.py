def solution():
    # Calculate the percentage of red and white jelly beans in the one bag
    red_percentage = (24 + 18) / (24 + 13 + 36 + 28 + 32 + 18)
    white_percentage = (18 + 24) / (24 + 13 + 36 + 28 + 32 + 18)

    # Estimate the number of red and white jelly beans in one bag
    red_white_bag = int(3 * (red_percentage + white_percentage))

    # Calculate the estimated total number of red and white jelly beans in the fishbowl
    red_white_fishbowl = red_white_bag * 3

    result = red_white_fishbowl
    return result

print(solution())