def solution():
    
    number_of_goldfish = 50
    ounces_of_food_per_goldfish = 1.5
    total_ounces_of_food_per_day = number_of_goldfish * ounces_of_food_per_goldfish
    special_food_percentage = 0.2
    ounces_of_special_food_per_day = total_ounces_of_food_per_day * special_food_percentage
    cost_of_special_food_per_ounce = 3
    total_cost_of_special_food_per_day = ounces_of_special_food_per_day * cost_of_special_food_per_ounce
    result = total_cost_of_special_food_per_day
    return result

print(solution())