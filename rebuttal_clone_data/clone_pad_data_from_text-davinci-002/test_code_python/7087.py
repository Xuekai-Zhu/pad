def solution():
    total_hours_needed = 1500
    hours_completed = 50 + 9 + 121
    hours_remaining = total_hours_needed - hours_completed
    months_remaining = 6
    hours_per_month = hours_remaining / months_remaining
    result = hours_per_month
    
    return result

print(solution())