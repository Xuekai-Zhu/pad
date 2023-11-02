def solution():
    
    starting_money = 2000
    furniture_cost = 400
    remaining_money = starting_money - furniture_cost
    anna_share = 0.75 * remaining_money
    emma_remaining = remaining_money - anna_share
    result = emma_remaining
    return result

print(solution())