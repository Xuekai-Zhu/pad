def solution():
    days_in_summer = 15 * 6  # Mr. Roper cuts his lawn 15 days a month from April to September, for a total of 6 months
    days_in_winter = 3 * 6  # Mr. Roper cuts his lawn 3 times a month from October to March, for a total of 6 months

    # Calculate the total number of times Mr. Roper cuts his yard in a year
    total_cuts = days_in_summer + days_in_winter

    # Calculate the average number of times Mr. Roper cuts his yard per month
    avg_cuts_per_month = total_cuts / 12
    result = avg_cuts_per_month
    return result

print(solution())