def solution():
    monday_study_time = 4
    tuesday_study_time = 2 * monday_study_time
    wed_thurs_fri_study_time = 3 * 3
    total_study_time = 25

    # Calculate the total study time for Monday and Tuesday combined
    monday_tuesday_study_time = monday_study_time + tuesday_study_time

    # Calculate the total study time for Monday to Friday combined
    total_weekday_study_time = monday_tuesday_study_time + wed_thurs_fri_study_time

    # Calculate the remaining study time for Saturday and Sunday
    remaining_study_time = total_study_time - total_weekday_study_time

    # Calculate the study time for Saturday
    saturday_study_time = remaining_study_time / 2
    result = saturday_study_time
    return result

print(solution())