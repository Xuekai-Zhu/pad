def solution():
    """John decides to fix a racecar. It cost $20,000 to fix but he gets a 20% discount. He wins his first race but only keeps 90% of the money. The prize is $70,000. How much money did he make from the car?"""
    fix_cost = 20000
    discount = 0.2
    final_fix_cost = fix_cost - (fix_cost * discount)
    prize_money = 70000
    winnings = prize_money * 0.9
    net_profit = winnings - final_fix_cost
    result = net_profit
    return result

print(solution())