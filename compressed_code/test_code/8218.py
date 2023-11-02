def solution():
    
    rate = 10
    first_month_hours = 35
    second_month_hours = first_month_hours + 5
    total_hours = first_month_hours + second_month_hours
    earnings = rate * total_hours
    personal_needs = earnings * (4/5)
    savings = earnings - personal_needs
    
    result = savings
    return result

print(solution())