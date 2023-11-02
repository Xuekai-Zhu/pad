def solution():
    
    monica_money = 15
    michelle_money = 12
    total_money = monica_money + michelle_money
    soda_price = 3
    cake_price = 15
    remaining_money = total_money - cake_price
    num_bottles = remaining_money // soda_price
    num_servings = num_bottles * 12
    servings_per_guest = num_servings // 8
    result = servings_per_guest
    
    return result

print(solution())