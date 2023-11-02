def solution():
    # Calculate the total number of days Kelly spent on vacation
    total_days = 3*7 - 1  # three weeks of vacation, minus the first day traveling
    sister_days = total_days - 5 - 1 - 5 - 2 - 2  # subtract the days spent at Grandparents', brother's, and traveling
    result = sister_days
    return result

print(solution())