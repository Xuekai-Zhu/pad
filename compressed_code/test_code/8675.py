def solution():
    
    num_adults = 6
    num_children = 2
    adult_meal_cost = 6
    child_meal_cost = 4
    soda_cost = 2
    total_cost = (num_adults * (adult_meal_cost + soda_cost)) + (num_children * (child_meal_cost + soda_cost))
    result = total_cost
    return result

print(solution())