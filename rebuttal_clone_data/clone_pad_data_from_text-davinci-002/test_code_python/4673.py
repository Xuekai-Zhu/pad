def solution():
    toy_organizers = 3 * 78
    gaming_chairs = 2 * 83
    total_sales = toy_organizers + gaming_chairs
    delivery_fee = total_sales * 0.05
    total_cost = total_sales + delivery_fee
    result = total_cost
    
    return result

print(solution())