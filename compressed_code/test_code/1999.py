def solution():
    
    fix_cost = 20000
    discount = 0.2
    final_fix_cost = fix_cost - (fix_cost * discount)
    prize_money = 70000
    winnings = prize_money * 0.9
    net_profit = winnings - final_fix_cost
    result = net_profit
    return result

print(solution())