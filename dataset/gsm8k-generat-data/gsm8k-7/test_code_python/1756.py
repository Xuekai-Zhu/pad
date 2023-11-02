def solution():
    rent = 1200
    groceries = 400
    medical = 200
    utilities = 60
    emergency = 200
    total_expenses = rent + groceries + medical + utilities + emergency
    
    hourly_rate = 15
    hours_needed = total_expenses / hourly_rate
    result = hours_needed
    return result

print(solution())