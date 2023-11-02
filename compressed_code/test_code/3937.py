def solution():
    
    evening_ticket_cost = 10
    food_combo_cost = 10
    discount_percentage = 0.2
    discount_food_percentage = 0.5
    discounted_ticket_cost = evening_ticket_cost * (1 - discount_percentage)
    discounted_food_combo_cost = food_combo_cost * (1 - discount_food_percentage)
    total_cost_evening = evening_ticket_cost + food_combo_cost
    total_cost_discounted = discounted_ticket_cost + discounted_food_combo_cost
    saved_money = total_cost_evening - total_cost_discounted
    result = saved_money
    return result

print(solution())