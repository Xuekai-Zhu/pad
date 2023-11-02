def solution():
    
    monday_appointments = 5
    monday_appointment_duration = 1.5
    tuesday_appointment_duration = 3
    thursday_appointments = 2
    thursday_appointment_duration = 2
    saturday_appointment_duration = 6

    total_hours = (monday_appointments * monday_appointment_duration) + tuesday_appointment_duration + (
                thursday_appointments * thursday_appointment_duration) + saturday_appointment_duration
    hourly_rate = 20
    total_payment = total_hours * hourly_rate
    result = total_payment
    return result

print(solution())