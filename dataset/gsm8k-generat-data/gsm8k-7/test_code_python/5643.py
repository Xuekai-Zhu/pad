def solution():
    vacuuming_time_per_session = 30  # minutes
    num_vacuuming_sessions_per_week = 3
    dusting_time_per_session = 20  # minutes
    num_dusting_sessions_per_week = 2

    # Calculate the total time spent vacuuming per week
    total_vacuuming_time = vacuuming_time_per_session * num_vacuuming_sessions_per_week

    # Calculate the total time spent dusting per week
    total_dusting_time = dusting_time_per_session * num_dusting_sessions_per_week

    # Calculate the total time spent cleaning per week
    total_cleaning_time = total_vacuuming_time + total_dusting_time
    result = total_cleaning_time
    return result

print(solution())