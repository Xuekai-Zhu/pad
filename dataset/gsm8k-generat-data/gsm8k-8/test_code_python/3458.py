def solution():
    # Calculate Jake's weekly deliveries
    jake_deliveries = 234

    # Calculate Miranda's weekly deliveries (twice as many as Jake's)
    miranda_deliveries = 2 * jake_deliveries

    # Calculate the difference in their weekly deliveries
    weekly_difference = miranda_deliveries - jake_deliveries

    # Calculate the monthly difference (4 weeks in a month)
    monthly_difference = weekly_difference * 4

    result = monthly_difference
    return result

print(solution())