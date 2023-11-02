def solution():
    
    num_sheep = 200
    pay_shearer = 2000
    total_wool = num_sheep * 10
    price_per_pound = 20
    revenue = total_wool * price_per_pound
    profit = revenue - pay_shearer
    result = profit
    return result

print(solution())