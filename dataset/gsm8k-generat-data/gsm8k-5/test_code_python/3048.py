def solution():
    # Calculate the number of teachers who walk out after one hour
    first_hour_walkouts = 0.5 * 60  # 50% of 60 substitute teachers

    # Calculate the remaining number of teachers
    remaining_teachers = 60 - first_hour_walkouts

    # Calculate the number of teachers who quit before lunch
    lunchtime_quitters = 0.3 * remaining_teachers

    # Calculate the final number of teachers left after lunch
    final_count = remaining_teachers - lunchtime_quitters
    result = final_count
    return result

print(solution())