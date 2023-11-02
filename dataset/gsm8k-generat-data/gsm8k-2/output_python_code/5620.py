def solution():
    """Lawrence worked 8 hours each day on Monday, Tuesday and Friday. He worked 5.5 hours on both Wednesday and Thursday. How many hours would Lawrence work each day if he worked the same number of hours each day?"""
    total_hours = (8 * 3) + (5.5 * 2)
    days_worked = 5
    equal_hours = total_hours / days_worked
    result = equal_hours
    return result

print(solution())