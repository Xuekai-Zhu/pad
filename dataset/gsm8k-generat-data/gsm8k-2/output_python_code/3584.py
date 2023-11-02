def solution():
    """Colt and Curt prepared 113 meals to be given away to a charity. Unexpectedly, Sole Mart provided 50 more meals. If Colt and Curt have given 85 meals already, how many more meals are left to be distributed?"""
    initial_meals = 113
    extra_meals = 50
    given_meals = 85
    remaining_meals = initial_meals + extra_meals - given_meals
    result = remaining_meals
    return result

print(solution())