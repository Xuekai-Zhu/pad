def solution():
    
    days_per_week = 3
    lifting_hours = 1
    cardio_hours = lifting_hours / 3
    total_hours = lifting_hours + cardio_hours
    result = total_hours * days_per_week
    return result

print(solution())