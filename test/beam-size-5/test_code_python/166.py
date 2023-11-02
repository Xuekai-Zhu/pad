def solution():
    
    hat_cost = 25
    jacket_cost = hat_cost * 3
    pants_cost = (hat_cost + jacket_cost) / 2
    total_cost = hat_cost + jacket_cost + pants_cost
    cost_per_uniform = total_cost / 3
    result = cost_per_uniform
    return result

print(solution())