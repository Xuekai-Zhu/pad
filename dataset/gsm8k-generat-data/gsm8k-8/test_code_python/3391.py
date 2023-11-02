def solution():
    # Calculate the total number of days in the vacation
    total_days = 21

    # Subtract the days spent traveling and at the grandparents' and brother's houses
    days_spent_elsewhere = 1 + 5 + 1 + 5 + 2 + 2
    days_at_sisters = total_days - days_spent_elsewhere

    result = days_at_sisters
    return result

print(solution())