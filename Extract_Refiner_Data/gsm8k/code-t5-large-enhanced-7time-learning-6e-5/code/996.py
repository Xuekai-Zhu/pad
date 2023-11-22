def solution():
    
    # Define the time it takes to check each type of trip
    INPATIENT_TIME = 20
    APPENDEES_TIME = 30

    # Define the number of inpatients and appointments
    num_inpatients = 9
    num_appointments = 10

    # Calculate the total time spent on all inpatients
    total_inpatient_time = num_inpatients * INPATIENT_TIME

    # Calculate the total time spent on all appointments
    total_appointment_time = num_appointments * APPENDEES_TIME

    # Calculate the total time spent on all trips
    total_trips_time = total_inpatient_time + total_appointment_time

    # Calculate the time left to update the records
    time_left = 9 * INPATIENT_TIME + total_trips_time - total_trips_time

    # Display the time left to update the records
    result = time_left
    return result

print(solution())