def solution():
    # Calculate the total time needed for every student to present their project
    total_time_per_student = 5  # in minutes
    total_time_needed = total_time_per_student * 32  # for all 32 students

    # Calculate the number of periods needed
    period_length = 40  # in minutes
    periods_needed = total_time_needed / period_length

    # Round up to the nearest integer
    periods_needed = math.ceil(periods_needed)

    result = periods_needed
    return result

print(solution())