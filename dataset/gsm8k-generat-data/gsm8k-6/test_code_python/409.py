def solution():
    total_days = 30
    quota = 50

    # Calculate the number of cars sold in the first week
    sold_first_week = 5*3 + 3*4  # first 3 days he sold 5 cars each day, next 4 days he sold 3 cars each day

    # Calculate the number of days remaining in the month
    days_remaining = total_days - 7

    # Calculate the number of cars Frank needs to sell in the remaining days to meet his quota
    cars_remaining = quota - sold_first_week
    cars_per_day = cars_remaining/days_remaining

    result = cars_per_day
    return result

print(solution())