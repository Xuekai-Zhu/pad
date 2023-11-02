def solution():
    """Mr. Roper cuts his lawn 15 days a month beginning in April and ending in September. From October to the end of March he cuts his lawn three times a month. What is the average number of times that Mr. Roper cuts his yard per month?"""
    april_september_months = 6
    october_march_months = 6
    april_september_cuts = 15 * april_september_months
    october_march_cuts = 3 * october_march_months
    total_cuts = april_september_cuts + october_march_cuts
    average_cuts_per_month = total_cuts / 12
    result = average_cuts_per_month
    return result

print(solution())