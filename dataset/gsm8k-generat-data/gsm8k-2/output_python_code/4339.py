def solution():
    """Claudia offers art classes to kids and charges $10.00 for her one-hour class. If 20 kids attend Saturday’s class and half that many attend Sunday’s class, how much money does she make?"""
    saturday_attendees = 20
    sunday_attendees = saturday_attendees / 2
    hourly_rate = 10
    saturday_earnings = saturday_attendees * hourly_rate
    sunday_earnings = sunday_attendees * hourly_rate
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())