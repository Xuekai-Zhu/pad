def solution():
    """Marta works on her grandparent's farm to raise money for a new phone. So far, she has collected $240. For every hour she works, she receives $10. Her grandmother often gives her tips, and she has collected $50 in tips in total. How many hours has Marta worked on the farm so far?"""
    total_money_collected = 240 + 50
    hourly_rate = 10
    hours_worked = total_money_collected / hourly_rate
    result = hours_worked
    return result

print(solution())