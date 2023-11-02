def solution():
    """Jerry works five days a week as a waiter and earns a variable amount of tips every night. The past four nights, he earned $20, $60, $15, and $40. How much does he need to earn tonight if he wants to make an average of $50 in tips per night?"""
    total_tips = 20 + 60 + 15 + 40
    target_avg = 50
    target_total = 5 * target_avg
    remaining_tips_needed = target_total - total_tips
    result = remaining_tips_needed
    return result

print(solution())