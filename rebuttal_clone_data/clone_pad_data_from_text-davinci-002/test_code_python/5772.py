def solution():
    cost_of_sweater = 9
    cost_of_t_shirt = 11
    cost_of_shoes = 30
    refund_amount = cost_of_shoes * 0.90
    total_cost = cost_of_sweater + cost_of_t_shirt + cost_of_shoes
    money_left = total_cost - refund_amount
    result = money_left
    
    return result

print(solution())