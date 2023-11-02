def solution():
    # Total income from selling mushrooms on the first day
    income_first_day = 58

    # Number of mushrooms picked on the second day
    mushrooms_second_day = 12

    # Number of mushrooms picked on the third day
    mushrooms_third_day = mushrooms_second_day * 2

    # Total number of mushrooms picked
    total_mushrooms = mushrooms_second_day + mushrooms_third_day

    # Total income from selling all mushrooms
    total_income = income_first_day + (total_mushrooms * 2)

    result = total_mushrooms
    return result

print(solution())