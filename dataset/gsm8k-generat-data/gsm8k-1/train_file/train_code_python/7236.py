def solution():
    """Jack has $43 in his piggy bank. He also gets an allowance of $10 a week. If Jack puts half of his allowance into his piggy bank every week, after 8 weeks how much will Jack have in his piggy bank?"""
    initial_amount = 43
    weekly_allowance = 10
    weeks = 8
    half_allowance = weekly_allowance / 2
    savings = half_allowance * weeks
    total_amount = initial_amount + savings
    result = total_amount
    return result

print(solution())