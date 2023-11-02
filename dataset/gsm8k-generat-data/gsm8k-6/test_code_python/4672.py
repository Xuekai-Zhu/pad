def solution():
    # Calculate the total amount of money Amanda will make this week
    monday_appointments = 5 * 1.5  # she has 5 1.5 hour appointments on Monday
    tuesday_appointment = 3  
    thursday_appointments = 2 * 2  # she has 2 2-hour appointments on Thursday
    saturday_appointment = 6  
    total_hours = monday_appointments + tuesday_appointment + thursday_appointments + saturday_appointment  # total number of hours worked 
    total_money = total_hours * 20.00  # she charges $20.00 per hour 
    result = total_money
    return result

print(solution())