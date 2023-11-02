def solution():
    # Calculate the total study time for Monday, Tuesday, Wednesday, Thursday, and Friday
    total_weekday_study_time = 4 + (2 * 4) + (3 * 3)

    # Calculate the remaining study time for the week
    remaining_study_time = 25 - total_weekday_study_time

    # Divide the remaining study time evenly between Saturday and Sunday
    saturday_study_time = remaining_study_time / 2

    result = saturday_study_time
    return result

print(solution())