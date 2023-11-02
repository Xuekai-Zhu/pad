def solution():
    total_cost = 85
    cost_of_three_shirts = 15 * 3
    cost_of_two_shirts = total_cost - cost_of_three_shirts
    cost_of_one_shirt = cost_of_two_shirts / 2
    result = cost_of_one_shirt
    return result

print(solution())