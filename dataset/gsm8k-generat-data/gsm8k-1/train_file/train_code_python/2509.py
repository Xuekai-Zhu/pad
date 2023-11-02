def solution():
    """Lindsey saved $50 in September, she saved $37 in October, and $11 in November. Lindsey's mom said that since Lindsey had saved more than $75, she would give Lindsey $25. Then Lindsey spent $87 on a video game. How much money did Lindsey have left?"""
    savings = 50 + 37 + 11
    if savings > 75:
        savings += 25
    total_spent = 87
    money_left = savings - total_spent
    result = money_left
    return result

print(solution())