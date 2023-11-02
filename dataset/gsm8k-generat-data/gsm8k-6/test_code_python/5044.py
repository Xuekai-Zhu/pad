def solution():
    # Calculate the number of half-day students
    half_day_students = 0.25 * 80

    # Calculate the number of full-day students
    full_day_students = 80 - half_day_students
    result = full_day_students
    return result

print(solution())