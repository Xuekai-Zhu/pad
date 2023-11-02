def solution():
    # Define the number of days in one week
    num_days = 7

    # Calculate the total number of hours 5th grade needs to read to beat 6th grade by 1 hour per student
    total_hours = 299 + 20 * num_days + 1

    # Calculate the number of hours each 5th grade student needs to read per day to beat 6th grade by 1 hour per student
    hours_per_student_per_day = total_hours / (20 * num_days)

    result = hours_per_student_per_day
    return result

print(solution())