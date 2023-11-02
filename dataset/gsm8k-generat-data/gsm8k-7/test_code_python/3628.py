def solution():
    target_savings = 75
    chores_per_week = 12
    extra_pay_rate = 2
    num_weeks = 2
    num_extra_chores = (4 * 7 - chores_per_week) * num_weeks

    # Calculate the total earnings from extra chores
    total_earnings = num_extra_chores * extra_pay_rate

    result = total_earnings
    return result

print(solution())