def solution():
    
    total_money = 150
    remaining_money = 25
    skates_cost = total_money / 2
    pads_cost = total_money - skates_cost - remaining_money
    result = pads_cost
    return result

print(solution())