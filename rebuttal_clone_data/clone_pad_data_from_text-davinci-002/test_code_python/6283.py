def solution():
    cost_of_tickets = 100 * 2
    cost_of_dinner = 120
    cost_of_limo = 80 * 6
    cost_of_tip = (cost_of_dinner + cost_of_limo) * .3
    total_cost = cost_of_tickets + cost_of_dinner + cost_of_limo + cost_of_tip
    result = total_cost
    
    return result

print(solution())