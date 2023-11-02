def solution():
    
    monica_money = 15
    michelle_money = 12
    cake_cost = 15
    soda_cost = 3
    total_money = monica_money + michelle_money
    remaining_money = total_money - cake_cost
    soda_count = remaining_money // soda_cost
    soda_servings = soda_count * 12
    servings_per_guest = soda_servings // 8
    result = servings_per_guest
    return result

print(solution())