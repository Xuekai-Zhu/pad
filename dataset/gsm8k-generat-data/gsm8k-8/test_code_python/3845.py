def solution():
    # Calculate the total number of mushrooms picked on the second day
    mushrooms_second_day = 12

    # Calculate the total number of mushrooms picked on the third day
    mushrooms_third_day = 2 * mushrooms_second_day

    # Calculate the total number of mushrooms picked during the trip
    total_mushrooms = mushrooms_second_day + mushrooms_third_day

    # Calculate the total amount earned from mushroom sales
    total_earnings = 58 + (total_mushrooms * 2)

    result = total_mushrooms
    return result

print(solution())