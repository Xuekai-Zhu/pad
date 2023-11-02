def solution():
    study_time_monday = 4
    study_time_tuesday = 2 * study_time_monday
    study_time_wednesday = 3
    study_time_thursday = 3
    study_time_friday = 3
    total_study_time = study_time_monday + study_time_tuesday + study_time_wednesday + study_time_thursday + study_time_friday
    remaining_study_time = 25 - total_study_time
    study_time_saturday = remaining_study_time / 2
    result = study_time_saturday
    return result

print(solution())