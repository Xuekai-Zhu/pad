def solution():
    
    starting_money = 100
    water_bottles = 4
    additional_bottles = 2 * water_bottles
    bottle_cost = 2
    cheese_cost_per_pound = 10
    cheese_weight = 0.5
    total_spent = (water_bottles + additional_bottles) * bottle_cost + cheese_weight * cheese_cost_per_pound
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())