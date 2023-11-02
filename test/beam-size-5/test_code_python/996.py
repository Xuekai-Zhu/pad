def solution():
    
    total_time = 9 * 60  # convert 9 inpatients to minutes
    time_per_inpatient = 20
    num_appointments = 10
    time_per_appointment = 30
    total_time_spent = time_per_inpatient * num_appointments
    time_left = total_time - total_time_spent
    result = time_left
    return result

print(solution())