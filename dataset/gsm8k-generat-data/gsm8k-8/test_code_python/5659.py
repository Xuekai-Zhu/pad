def solution():
    # Calculate the number of visitors in November
    november_visitors = 100 * 1.15

    # Calculate the number of visitors in December
    december_visitors = november_visitors + 15

    # Calculate the total number of visitors for the three months
    total_visitors = 100 + november_visitors + december_visitors
    result = total_visitors
    return result

print(solution())