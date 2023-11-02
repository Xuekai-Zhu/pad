def solution():
    """Jackson wants to go on a shopping spree, so his mom says she will give him some spending money if he does extra chores. She promises $5 per hour spent on chores. Jackson spends 2 hours vacuuming, and decides to do this twice. He also spends 0.5 hours washing dishes, and three times as long cleaning the bathroom. How much spending money has Jackson earned?"""
    hourly_pay = 5
    vacuuming_time = 2 * 2
    dishes_time = 0.5
    bathroom_time = 3 * dishes_time
    total_time = vacuuming_time + dishes_time + bathroom_time
    total_pay = total_time * hourly_pay
    result = total_pay
    return result

print(solution())