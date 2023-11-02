def solution():
    num_students = 32
    presentation_time = 5 # minutes
    period_length = 40 # minutes

    # Calculate the total time needed for all students to present
    total_time_needed = num_students * presentation_time

    # Calculate the number of periods needed to complete all presentations
    periods_needed = total_time_needed / period_length
    result = periods_needed
    return result

print(solution())