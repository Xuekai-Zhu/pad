def solution():
    """Keegan was running a car wash with his friend Tashay to raise money for a baseball camp. They needed to raise $200 for the two of them. By 3 pm, Keegan had earned $83 and Tasha had earned $91. How much more did they need to earn to reach their goal?"""
    goal = 200
    current_earnings = 83 + 91
    remaining = goal - current_earnings
    result = remaining
    return result

print(solution())