def solution():
    
    chicken_meal_cost = 12
    milk_packs_cost = 5
    apple_cost = 1.5
    total_cost = 50
    chicken_meal_total = chicken_meal_cost
    milk_total = milk_packs_cost * milk_packs_cost
    apple_total = apple_cost * 4
    pizza_total = total_cost - chicken_meal_total - milk_total - apple_total
    pizza_boxes = pizza_total / 8.5
    result = pizza_boxes
    return result

print(solution())