def solution():
    # Calculate the number of visitors in November
    november_visitors = 100 * 1.15  # 15% increase from October

    # Calculate the number of visitors in December
    december_visitors = november_visitors + 15

    # Calculate the total number of visitors for October, November, and December
    total_visitors = 100 + november_visitors + december_visitors
    result = total_visitors
    return result

print(solution())