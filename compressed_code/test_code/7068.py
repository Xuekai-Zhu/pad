def solution():
    
    new_visitors_per_hour = 50
    hours_open_per_day = 8
    total_visitors = new_visitors_per_hour * hours_open_per_day
    visitors_to_gorilla_exhibit = total_visitors * 0.8
    result = visitors_to_gorilla_exhibit
    return result

print(solution())