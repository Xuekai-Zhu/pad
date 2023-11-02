def solution():
    """John decides to fix a racecar. It cost $20,000 to fix but he gets a 20% discount. He wins his first race but only keeps 90% of the money. The prize is $70,000. How much money did he make from the car?"""
    repair_cost = 20000
    discount_percent = 20
    discount_amount = repair_cost * (discount_percent / 100)
    total_cost = repair_cost - discount_amount
    prize_money = 70000
    net_prize_money = prize_money * 0.9
    profit = net_prize_money - total_cost
    result = profit
    return result

print(solution())