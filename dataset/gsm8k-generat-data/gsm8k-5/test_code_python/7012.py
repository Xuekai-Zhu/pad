def solution():
    jacob_hourly_pay = 6  # Jacob earns $6 per hour
    jake_hourly_pay = jacob_hourly_pay * 3  # Jake earns thrice what Jacob does
    jake_total_earnings = jake_hourly_pay * 8 * 5  # Jake works 8 hours a day for 5 days

    result = jake_total_earnings
    return result

print(solution())