def solution():
    hourly_pay = 8  # Carrie's hourly pay
    hours_per_week = 35  # number of hours Carrie works per week
    weeks_in_month = 4  # number of weeks in a month
    total_earnings = hourly_pay * hours_per_week * weeks_in_month  # total earnings in a month
    bike_price = 400  # price of the bike
    money_left_over = total_earnings - bike_price  # money left over after buying the bike
    result = money_left_over
    return result

print(solution())