def solution():
    
    rock_weight = 1.5
    price_per_pound = 4
    total_price = 60
    total_weight = total_price / price_per_pound
    total_rocks = int(total_weight / rock_weight)
    result = total_rocks
    return result

print(solution())