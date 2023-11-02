def solution():
    
    weeks_before_raise = 8
    allowance_before_raise = 5
    weeks_after_raise = 6
    allowance_after_raise = 6
    clothes_cost = (weeks_before_raise * allowance_before_raise + weeks_after_raise * allowance_after_raise) / 2
    remaining_money = (weeks_before_raise * allowance_before_raise + weeks_after_raise * allowance_after_raise - clothes_cost) - 35
    result = remaining_money
    return result

print(solution())