def solution():
    monday_visitors = 50
    tuesday_visitors = monday_visitors * 2
    other_days_visitors = 20 * 5  # 5 remaining days of the week

    # Total number of visitors for the week
    total_visitors = monday_visitors + tuesday_visitors + other_days_visitors
    result = total_visitors
    return result

print(solution())