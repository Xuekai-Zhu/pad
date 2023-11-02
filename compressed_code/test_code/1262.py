def solution():
    
    new_visitors_per_hour = 50
    open_hours_per_day = 8
    total_visitors = new_visitors_per_hour * open_hours_per_day
    gorilla_visitors = 0.8 * total_visitors
    result = gorilla_visitors
    return result

print(solution())