def solution():
    local_call_cost = 0.05
    international_call_cost = 0.25
    dad_call_duration = 45
    brother_call_duration = 31

    # Calculate the cost of calling his dad
    dad_call_cost = dad_call_duration * local_call_cost

    # Calculate the cost of calling his brother
    brother_call_cost = brother_call_duration * international_call_cost

    # Calculate the total cost of all calls
    total_cost = dad_call_cost + brother_call_cost
    result = total_cost
    return result

print(solution())