def solution():
    monday_visitors = 50
    tuesday_visitors = monday_visitors * 2
    rest_of_week_visitors = (20 * 5)
    total_visitors = monday_visitors + tuesday_visitors + rest_of_week_visitors
    result = total_visitors
    return result

print(solution())