def solution():
    # Calculate the number of cherry tomatoes
    mushrooms = 3
    cherry_tomatoes = 2 * mushrooms

    # Calculate the number of pickles
    pickles = 4 * cherry_tomatoes

    # Calculate the number of bacon bits
    bacon_bits = 4 * pickles

    # Calculate the number of red bacon bits
    red_bacon_bits = bacon_bits // 3

    result = red_bacon_bits
    return result

print(solution())