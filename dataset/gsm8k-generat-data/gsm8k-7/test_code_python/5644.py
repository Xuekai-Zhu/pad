def solution():
    num_appointments = 2
    appointment_length = 3
    workday_hours = 8

    # Calculate the total time spent in appointments
    total_appointment_time = num_appointments * appointment_length

    # Calculate the total time spent stamping permits
    total_stamp_time = workday_hours - total_appointment_time

    # Calculate the total number of permits stamped
    permits_stamped = total_stamp_time * 50

    result = permits_stamped
    return result

print(solution())