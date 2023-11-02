def solution():
    
    tv_cost = 50
    num_tvs = 5
    total_tv_cost = tv_cost * num_tvs
    total_spent = 260
    figurine_cost = (total_spent - total_tv_cost) / 10
    result = figurine_cost
    return result

print(solution())