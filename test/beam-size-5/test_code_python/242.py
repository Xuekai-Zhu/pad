def solution():
    
    hourly_rate = 250
    hours_per_day = 6
    hours_per_week = 4
    weeks_to_finish = 5
    total_hours_needed = hours_per_day * hours_per_week * weeks_to_finish
    total_hours_done = total_hours_needed * hours_per_week
    total_hours_remaining = total_hours_needed - total_hours_done
    total_cost = total_hours_remaining * hourly_rate
    discount = total_cost * 0.1
    final_cost = total_cost - discount
    result = final_cost
    return result

print(solution())