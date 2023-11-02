def solution():
    """Shara collects shells. She had 20 shells before she went on vacation. On vacation, she found 5 shells per day for 3 days. Then he found 6 shells on the fourth day. How many shells does she have now?"""
    starting_shells = 20
    shells_per_day = 5
    vacation_days = 3
    additional_shells = shells_per_day * vacation_days
    fourth_day_shells = 6
    total_shells = starting_shells + additional_shells + fourth_day_shells
    result = total_shells
    return result

print(solution())