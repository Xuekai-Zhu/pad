def solution():
    """Amanda charges $20.00 per hour to help clean out and organize a person's home. She has 5 1.5 hours appointments on Monday, a 3-hours appointment on Tuesday and 2 2-hours appointments on Thursday. On Saturday, she will spend 6 hours at one client's house. How much money will she make this week?"""
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