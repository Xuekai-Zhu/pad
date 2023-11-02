def solution():
    # Calculate the time needed per student's presentation (in minutes)
    presentation_time = 5

    # Calculate the total time needed for all students' presentations (in minutes)
    total_presentation_time = 32 * presentation_time

    # Calculate the number of periods needed (in 40-minute periods)
    periods_needed = total_presentation_time / 40

    # Round up to the nearest whole number of periods
    periods_needed = math.ceil(periods_needed)

    result = periods_needed
    return result

print(solution())