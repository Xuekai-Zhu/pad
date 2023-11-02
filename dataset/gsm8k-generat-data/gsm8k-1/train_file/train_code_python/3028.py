def solution():
    """Mr. Roper cuts his lawn 15 days a month beginning in April and ending in September. From October to the end of March he cuts his lawn three times a month. What is the average number of times that Mr. Roper cuts his yard per month?"""
    days_in_spring_summer = 6 * 15
    days_in_fall_winter = 6 * 3
    total_days = days_in_spring_summer + days_in_fall_winter
    total_cuts = 15 * 6 + 3 * 6
    average_cuts_per_month = total_cuts / total_days
    result = average_cuts_per_month
    return result

print(solution())