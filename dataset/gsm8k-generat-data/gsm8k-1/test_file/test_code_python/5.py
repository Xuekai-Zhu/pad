def solution():
    """Eliza's rate per hour for the first 40 hours she works each week is $10. She also receives an overtime pay of 1.2 times her regular hourly rate. If Eliza worked for 45 hours this week, how much are her earnings for this week?"""
    regular_rate = 10
    overtime_rate = 1.2 * regular_rate
    standard_hours = 40
    overtime_hours = 5
    total_earnings = (regular_rate * standard_hours) + (overtime_rate * overtime_hours)
    result = total_earnings
    return result

print(solution())