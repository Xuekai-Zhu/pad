def solution():
    monday_appointments = 5
    monday_hours = 1.5
    tuesday_appointments = 1
    tuesday_hours = 3
    thursday_appointments = 2
    thursday_hours = 2
    saturday_hours = 6
    hourly_rate = 20

    # Calculate the total hours Amanda spent on Monday
    monday_total_hours = monday_appointments * monday_hours

    # Calculate the total hours Amanda spent on Tuesday
    tuesday_total_hours = tuesday_appointments * tuesday_hours

    # Calculate the total hours Amanda spent on Thursday
    thursday_total_hours = thursday_appointments * thursday_hours

    # Calculate the total hours Amanda spent on Saturday
    saturday_total_hours = saturday_hours

    # Calculate the total hours Amanda spent during the week
    total_hours = monday_total_hours + tuesday_total_hours + thursday_total_hours + saturday_total_hours

    # Calculate the total amount of money Amanda will make
    total_income = total_hours * hourly_rate
    result = total_income
    return result

print(solution())