def solution():
    total_classrooms = 80  # The custodian has to clean a school with 80 classrooms
    num_days = 5  # The custodian has to clean the school for 5 days
    time_per_classroom = 15  # It takes the custodian 15 minutes per classroom
    hours_worked = 8  # The custodian works an 8 hour day

    # Calculate the total time spent cleaning classrooms
    total_time = num_days * time_per_classroom * hours_worked

    # Calculate the average time spent cleaning classrooms per day
    avg_classrooms_per_day = (total_time / total_classrooms) / total_time
    result = avg_classrooms_per_day
    return result

print(solution())