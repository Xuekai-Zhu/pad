def solution():
    """Hannah wants to save $80 for five weeks. In the first week, she saved $4 and she plans to save twice as much as her savings as the previous week. How much will she save in the fifth week to reach her goal?"""
    total_goal = 80
    current_savings = 4
    for i in range(2, 6):
        current_savings *= 2
        total_goal -= current_savings
    result = total_goal
    return result

print(solution())