def solution():
    """On Tuesday, Peter wants to exercise for twice the amount of time he did on Monday and Sunday combined. On Sunday he exercised for 23 minutes. On Monday he exercised for 16 minutes. How many minutes does he have to exercise on Tuesday to reach his goal?"""
    sunday_time = 23
    monday_time = 16
    combined_time = sunday_time + monday_time
    tuesday_goal = combined_time * 2
    tuesday_time = tuesday_goal - combined_time
    result = tuesday_time
    return result

print(solution())