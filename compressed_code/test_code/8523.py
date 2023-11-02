def solution():
    
    total_money = 80
    dinner_cost = total_money * 3/4
    remaining_money = total_money - dinner_cost - 2  
    cost_per_scoop = 1.5
    num_scoops_each = remaining_money / (cost_per_scoop * 2)  
    result = num_scoops_each
    return result

print(solution())