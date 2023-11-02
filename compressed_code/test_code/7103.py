def solution():
    
    rock_weight = 1.5
    price_per_pound = 4
    total_sale = 60
    total_weight = total_sale / price_per_pound 
    num_rocks = total_weight / rock_weight
    result = num_rocks
    return result

print(solution())