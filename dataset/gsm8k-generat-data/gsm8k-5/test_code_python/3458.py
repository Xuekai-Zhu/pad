def solution():
    jake_deliveries = 234  # Jake delivers 234 newspapers a week
    miranda_deliveries = 2 * jake_deliveries  # Miranda delivers twice as many newspapers as Jake
    weeks_in_month = 4  # There are 4 weeks in a month

    # Calculate the total number of newspapers delivered by Jake in a month
    jake_monthly_deliveries = jake_deliveries * weeks_in_month

    # Calculate the total number of newspapers delivered by Miranda in a month
    miranda_monthly_deliveries = miranda_deliveries * weeks_in_month

    # Calculate the difference in the number of newspapers delivered by Miranda and Jake in a month
    difference = miranda_monthly_deliveries - jake_monthly_deliveries
    result = difference
    return result

print(solution())