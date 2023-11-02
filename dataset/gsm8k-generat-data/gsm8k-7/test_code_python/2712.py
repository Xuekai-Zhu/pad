def solution():
    lesson_duration = 1  # hour
    cost_per_half_hour = 10
    num_weeks = 5
    
    # Calculate the total number of half-hours taught in 5 weeks
    total_half_hours = lesson_duration * 2 * num_weeks

    # Calculate the total amount of money the teacher would earn
    total_earnings = total_half_hours * cost_per_half_hour
    result = total_earnings
    return result

print(solution())