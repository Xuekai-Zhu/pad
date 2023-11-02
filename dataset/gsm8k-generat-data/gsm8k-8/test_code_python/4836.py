def solution():
    # Calculate the number of visits per day
    visits_per_day = 50 * 24

    # Calculate the number of visits in a 30 day month
    visits_per_month = visits_per_day * 30

    # Calculate the total amount earned in a 30 day month
    earnings = visits_per_month * 0.10

    result = earnings
    return result

print(solution())