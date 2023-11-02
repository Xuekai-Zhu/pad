def solution():
    """Lindsey saved $50 in September, she saved $37 in October, and $11 in November. Lindsey's mom said that since Lindsey had saved more than $75, she would give Lindsey $25. Then Lindsey spent $87 on a video game. How much money did Lindsey have left?"""
    total_savings = 50 + 37 + 11 + 25
    total_spent = 87
    remaining_money = total_savings - total_spent
    result = remaining_money
    return result

print(solution())