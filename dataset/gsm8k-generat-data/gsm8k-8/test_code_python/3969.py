def solution():
    # Define the extra minutes earned for each grade
    grade_to_extra_recess = {'A': 2, 'B': 1, 'C': 0, 'D': -1}

    # Calculate the total extra minutes earned
    total_extra_minutes = 10 * grade_to_extra_recess['A'] + 12 * grade_to_extra_recess['B'] \
                          + 5 * grade_to_extra_recess['D']

    # Calculate the total recess time, including the extra minutes
    total_recess_time = 20 + total_extra_minutes
    result = total_recess_time
    return result

print(solution())