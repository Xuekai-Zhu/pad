def solution():
    
    total_cost = 85
    cost_of_three_shirts = 3 * 15
    cost_of_two_remaining_shirts = total_cost - cost_of_three_shirts
    cost_of_one_remaining_shirt = cost_of_two_remaining_shirts / 2
    result = cost_of_one_remaining_shirt
    return result

print(solution())