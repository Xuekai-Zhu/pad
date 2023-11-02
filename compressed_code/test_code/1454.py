def solution():
    
    weeks1 = 8
    allowance1 = 5
    weeks2 = 6
    allowance2 = 6
    total_allowance = weeks1 * allowance1 + weeks2 * allowance2
    clothes_cost = total_allowance / 2
    remaining_money = total_allowance - clothes_cost - 35
    result = remaining_money
    return result

print(solution())