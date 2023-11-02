def solution():
    # Calculate the number of red glass pieces that Blanche and Rose found together
    red_total = 3 + 9

    # Calculate how many red glass pieces Dorothy found
    red_dorothy = 2 * red_total

    # Calculate the number of blue glass pieces that Rose found
    blue_rose = 11

    # Calculate how many blue glass pieces Dorothy found
    blue_dorothy = 3 * blue_rose

    # Calculate how many green glass pieces Blanche found
    green_blanche = 12

    # Calculate how many pieces of sea glass Dorothy collected in total
    total_dorothy = red_dorothy + blue_dorothy + green_blanche

    result = total_dorothy
    return result

print(solution())