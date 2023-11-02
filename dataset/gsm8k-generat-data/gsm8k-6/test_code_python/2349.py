def solution():
    # Calculate the cost of getting a burger meal and a soda
    burger_meal_cost = 6
    soda_cost = (1/3) * burger_meal_cost
    total_cost = (burger_meal_cost + soda_cost) * 2 + (burger_meal_cost + soda_cost) * 2
    result = total_cost
    return result

print(solution())