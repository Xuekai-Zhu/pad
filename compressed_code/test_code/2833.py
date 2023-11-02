def solution():
    
    adults = 6
    children = 2
    adult_meal_cost = 6
    children_meal_cost = 4
    soda_cost = 2
    total_cost = (adults * adult_meal_cost) + (children * children_meal_cost) + ((adults + children) * soda_cost)
    result = total_cost
    return result

print(solution())