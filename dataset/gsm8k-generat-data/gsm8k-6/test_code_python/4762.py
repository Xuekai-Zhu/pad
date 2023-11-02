def solution():
    # Calculate the total screen space of each TV
    tv1_screen_space = 48 * 100
    tv2_screen_space = 70 * 60

    # Calculate the weight of each TV in ounces
    tv1_weight = tv1_screen_space * 4
    tv2_weight = tv2_screen_space * 4

    # Calculate the weight difference in pounds
    weight_difference = (tv2_weight - tv1_weight) / 16

    result = weight_difference
    return result

print(solution())