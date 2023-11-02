def solution():
    
    dad_call_time = 45
    brother_call_time = 31
    local_call_cost = 0.05
    international_call_cost = 0.25
    dad_call_cost = dad_call_time * local_call_cost
    brother_call_cost = brother_call_time * international_call_cost
    total_cost = dad_call_cost + brother_call_cost
    result = total_cost
    return result

print(solution())