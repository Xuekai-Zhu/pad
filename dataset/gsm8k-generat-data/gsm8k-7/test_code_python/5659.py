def solution():
    october_visitors = 100
    november_increase = 0.15
    december_increase = 15

    # Calculate the number of visitors in November
    november_visitors = october_visitors * (1 + november_increase)

    # Calculate the number of visitors in December
    december_visitors = november_visitors + december_increase

    # Calculate the total number of visitors for the three months
    total_visitors = october_visitors + november_visitors + december_visitors
    result = total_visitors
    return result

print(solution())