def solution():
    """Jackson wants to go on a shopping spree, so his mom says she will give him some spending money if he does extra chores. She promises $5 per hour spent on chores. Jackson spends 2 hours vacuuming, and decides to do this twice. He also spends 0.5 hours washing dishes, and three times as long cleaning the bathroom. How much spending money has Jackson earned?"""
    vacuum_hours = 2
    vacuum_sessions = 2
    dishes_hours = 0.5
    bathroom_hours = 3 * dishes_hours
    total_hours = vacuum_hours * vacuum_sessions + dishes_hours + bathroom_hours
    pay_rate = 5
    spending_money = total_hours * pay_rate
    result = spending_money
    return result

print(solution())