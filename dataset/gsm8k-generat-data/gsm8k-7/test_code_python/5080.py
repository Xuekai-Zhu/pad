def solution():
    kimmie_earnings = 450
    zahra_earnings = kimmie_earnings - (1/3 * kimmie_earnings)
    total_earnings = kimmie_earnings + zahra_earnings
    joint_savings = total_earnings / 2
    result = joint_savings
    return result

print(solution())