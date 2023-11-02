def solution():
    pencils_per_day = 2  # Judy uses 2 pencils per day
    days_in_week = 5  # Judy goes to school 5 days a week
    weeks_in_period = 9  # Judy wants to know how much she will spend on pencils over 45 days

    # Calculate the total number of pencils Judy will use in 45 days
    total_pencils = pencils_per_day * days_in_week * weeks_in_period

    # Calculate the total cost of pencils Judy will buy in 45 days
    cost_total = 4 * ((total_pencils + 29) // 30)  # Round up to the nearest pack of pencils
    result = cost_total
    return result

print(solution())