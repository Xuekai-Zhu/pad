def solution():
    # Calculate how many apples Bella eats in a week
    bella_weekly_apples = 6 * 7

    # Calculate how many apples Grace picks for Bella in a week
    grace_weekly_apples = bella_weekly_apples * 3

    # Calculate how many apples Grace will have after 6 weeks
    grace_total_apples = grace_weekly_apples * 6

    result = grace_total_apples
    return result

print(solution())