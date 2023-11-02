def solution():
    """Melissa is summoned to jury duty. She spends 6 hours a day for 3 days listening to a court case. If Melissa is paid $15 per day but also has to pay $3 for parking each day, how much jury pay does she make per hour after expenses?"""
    hours_spent = 6 * 3
    daily_pay = 15 - 3
    total_pay = daily_pay * 3
    pay_per_hour = total_pay / hours_spent
    result = pay_per_hour
    return result

print(solution())