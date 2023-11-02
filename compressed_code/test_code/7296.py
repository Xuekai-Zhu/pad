def solution():
    
    days_in_june = 30
    videos_per_day = 10
    first_half_days = days_in_june / 2
    second_half_days = days_in_june - first_half_days
    first_half_hours = first_half_days * videos_per_day * 1
    second_half_hours = second_half_days * videos_per_day * 2
    total_hours = first_half_hours + second_half_hours
    result = total_hours
    return result

print(solution())