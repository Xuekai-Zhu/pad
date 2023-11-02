def solution():
    
    total_spent = 260
    tv_cost = 50
    tv_count = 5
    total_tv_cost = tv_cost * tv_count
    figurine_cost = (total_spent - total_tv_cost) / 10
    result = figurine_cost
    return result

print(solution())