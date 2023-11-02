def solution():
    
    total_chickens = 80
    chickens_sold_neighbor = 12
    chickens_sold_gate = 25
    chickens_left = total_chickens - chickens_sold_neighbor - chickens_sold_gate
    result = chickens_left
    return result

print(solution())