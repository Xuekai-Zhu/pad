def solution():
    tuesday_traffic = 25
    monday_traffic = 0.8 * tuesday_traffic
    wednesday_traffic = monday_traffic + 2
    thursday_traffic = friday_traffic = 10
    weekend_traffic = 5

    # Total traffic for the week
    total_weekly_traffic = tuesday_traffic + monday_traffic + wednesday_traffic + thursday_traffic + friday_traffic + 2 * weekend_traffic

    result = total_weekly_traffic
    return result

print(solution())