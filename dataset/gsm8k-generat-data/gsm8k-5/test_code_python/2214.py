def solution():
    total_time = 150  # Matt did his homework for 150 minutes
    math_time = 0.3 * total_time  # Matt spent 30% of the time on math
    science_time = 0.4 * total_time  # Matt spent 40% of the time on science

    # Calculate the time Matt spent on other subjects
    other_subjects_time = total_time - math_time - science_time
    result = other_subjects_time
    return result

print(solution())