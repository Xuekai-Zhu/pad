def solution():
    # Calculate the total hours Doris can work in a month
    total_hours = 3 * 5 * 4 + 5 * 4  # 3 hours per weekday (5 weekdays per week), and 5 hours on Saturday (4 Saturdays per month)

    # Calculate the total amount Doris can earn in a month
    total_income = 20 * total_hours

    # Calculate the number of weeks needed to earn at least $1200
    weeks_needed = int((1200 - total_income) / (20 * total_hours)) + 1

    result = weeks_needed
    return result

print(solution())