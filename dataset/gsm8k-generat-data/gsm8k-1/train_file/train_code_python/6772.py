def solution():
    """Jerry works five days a week as a waiter and earns a variable amount of tips every night. The past four nights, he earned $20, $60, $15, and $40. How much does he need to earn tonight if he wants to make an average of $50 in tips per night?"""
    total_tips_so_far = 20 + 60 + 15 + 40
    days_so_far = 4
    target_average = 50
    remaining_days = 5 - days_so_far
    total_tips_needed = target_average * 5 - total_tips_so_far
    tips_needed_per_day = total_tips_needed / remaining_days
    result = tips_needed_per_day
    return result

print(solution())