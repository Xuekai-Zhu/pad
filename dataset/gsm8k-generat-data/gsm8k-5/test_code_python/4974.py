def solution():
    days_per_week = 7
    days_off = 3
    days_streaming = days_per_week - days_off
    hours_per_stream = 4
    wage_per_hour = 10

    # Calculate the total amount John makes per week
    total_income = days_streaming * hours_per_stream * wage_per_hour

    result = total_income
    return result

print(solution())