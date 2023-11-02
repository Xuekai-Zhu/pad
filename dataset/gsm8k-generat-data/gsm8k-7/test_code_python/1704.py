def solution():
    num_mushrooms = 3

    # Calculate the number of cherry tomatoes based on the number of mushrooms
    num_cherry_tomatoes = num_mushrooms * 2

    # Calculate the number of pickles based on the number of cherry tomatoes
    num_pickles = num_cherry_tomatoes * 4

    # Calculate the total number of bacon bits based on the number of pickles
    num_bacon_bits = num_pickles * 4

    # Calculate the number of red bacon bits based on one third of the total bacon bits
    num_red_bacon_bits = num_bacon_bits / 3

    result = num_red_bacon_bits
    return result

print(solution())