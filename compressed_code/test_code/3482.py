def solution():
    
    total_savings = 6 + (5 * 6) + ((1/3) * (5 * 6))
    remaining_money = total_savings - 40
    each_girl_gets = remaining_money / 3
    result = each_girl_gets
    return result

print(solution())