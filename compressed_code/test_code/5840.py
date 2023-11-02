def solution():
    
    price_per_craft = 12
    num_crafts_sold = 3
    extra_money = 7
    total_money = (price_per_craft * num_crafts_sold) + extra_money
    deposit = 18
    remaining_money = total_money - deposit
    result = remaining_money
    
    return result

print(solution())