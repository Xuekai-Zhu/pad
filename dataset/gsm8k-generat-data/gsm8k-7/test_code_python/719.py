def solution():
    monday_visitors = 50
    tuesday_visitors = 2 * monday_visitors
    remaining_days_visitors = 20
    total_visitors = monday_visitors + tuesday_visitors + (remaining_days_visitors * 5)
    result = total_visitors
    return result

print(solution())