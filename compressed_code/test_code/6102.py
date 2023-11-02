def solution():
    
    starting_money = 55
    bananas_cost = 4 * 2
    pears_cost = 2
    asparagus_cost = 6
    chicken_cost = 11
    total_spent = bananas_cost + pears_cost + asparagus_cost + chicken_cost
    remaining_money = starting_money - total_spent
    result = remaining_money
    return result

print(solution())