def solution():
    
    monday_visitors = 50
    tuesday_visitors = monday_visitors * 2
    remaining_days = 5
    average_daily_visitors = 20
    total_visitors = monday_visitors + tuesday_visitors + (remaining_days * average_daily_visitors)
    result = total_visitors
    return result

print(solution())