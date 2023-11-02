def solution():
    machines = 10
    bearings_per_machine = 30
    cost_per_bearing = 1
    sale_cost_per_bearing = 0.75
    discount_percent = 20
    total_bearings = machines * bearings_per_machine
    cost_of_bearings = total_bearings * cost_per_bearing
    sale_cost_of_bearings = total_bearings * sale_cost_per_bearing
    discount_amount = sale_cost_of_bearings * (discount_percent / 100)
    final_cost = sale_cost_of_bearings - discount_amount
    savings = cost_of_bearings - final_cost
    result = savings
    
    return result

print(solution())