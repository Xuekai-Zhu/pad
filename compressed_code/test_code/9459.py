def solution():
    
    hourly_rate = 20
    monday_appointments = 5
    monday_hours = 1.5
    tuesday_appointments = 1
    tuesday_hours = 3
    thursday_appointments = 2
    thursday_hours = 2
    saturday_hours = 6
    total_hours = (monday_appointments * monday_hours) + (tuesday_appointments * tuesday_hours) + (thursday_appointments * thursday_hours) + saturday_hours
    total_earnings = total_hours * hourly_rate
    result = total_earnings
    return result

print(solution())