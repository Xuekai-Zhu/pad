def solution():
    call_duration = 30 # in minutes
    call_cost_per_minute = 0.05
    calls_per_week = 1 # assuming he calls once per week
    num_weeks_in_year = 52
    
    # Calculate the total number of minutes Noah talks on the phone in a year
    total_call_duration = call_duration * calls_per_week * num_weeks_in_year
    
    # Calculate the total cost of all phone calls in a year
    total_cost = total_call_duration * call_cost_per_minute
    result = total_cost
    return result

print(solution())