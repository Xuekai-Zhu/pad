def solution():
    
    saturday_attendees = 20
    sunday_attendees = saturday_attendees / 2
    hourly_rate = 10
    saturday_earnings = saturday_attendees * hourly_rate
    sunday_earnings = sunday_attendees * hourly_rate
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())