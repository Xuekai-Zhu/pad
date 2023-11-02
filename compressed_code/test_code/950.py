def solution():
    
    total_hours_in_3_days = 72
    travel_hours_before_first_break = 10 + 3 + 10 + 1
    travel_hours_per_cycle = 11
    break_hours_per_cycle = 1
    total_travel_hours = total_hours_in_3_days - travel_hours_before_first_break
    num_cycles = total_travel_hours // (travel_hours_per_cycle + break_hours_per_cycle)
    remaining_travel_hours = total_travel_hours - num_cycles * (travel_hours_per_cycle + break_hours_per_cycle)
    total_break_hours = num_cycles * break_hours_per_cycle + 4  
    result = total_break_hours
    return result

print(solution())