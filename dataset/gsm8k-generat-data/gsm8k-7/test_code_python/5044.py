def solution():
    total_students = 80
    half_day_percent = 0.25

    # Calculate the number of half-day students
    num_half_day = total_students * half_day_percent

    # Calculate the number of full-day students
    num_full_day = total_students - num_half_day
    result = num_full_day
    return result

print(solution())