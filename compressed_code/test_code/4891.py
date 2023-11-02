def solution():
    
    mango_price = 3
    juice_price = 3
    num_mangoes = 6
    num_juice = 6
    total_cost = (mango_price * num_mangoes) + (juice_price * num_juice)
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())