def solution():
    
    
    beef_cost = 11 * 3
    fruits_veggies_cost = 8 * 4
    spices_cost = 6 * 3
    other_groceries_cost = 37
    total_spent = beef_cost + fruits_veggies_cost + spices_cost + other_groceries_cost
    
    bonus_points = 0
    if total_spent > 100:
        bonus_points = 250
    
    points_per_ten = 50
    total_points = (total_spent // 10) * points_per_ten + bonus_points
    
    result = total_points
    return result

print(solution())