def solution():
    num_pants = 2
    num_shirts = 5
    total_cost = 62

    # Calculate the cost of each shirt for Jessica
    cost_per_shirt = 20 / 2

    # Calculate the cost of each pair of pants for Peter
    cost_per_pant = (total_cost - (num_shirts * cost_per_shirt)) / num_pants
    
    result = cost_per_pant
    return result

print(solution())