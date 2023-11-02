def solution():
    """Claudia offers art classes to kids and charges $10.00 for her one-hour class. If 20 kids attend Saturday’s class and half that many attend Sunday’s class, how much money does she make?"""
    saturday_attendees = 20
    sunday_attendees = saturday_attendees / 2
    class_price = 10.00
    saturday_earnings = saturday_attendees * class_price
    sunday_earnings = sunday_attendees * class_price
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())