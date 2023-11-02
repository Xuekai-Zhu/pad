def solution():
    
    saturday_attendees = 20
    sunday_attendees = saturday_attendees / 2
    class_price = 10.00
    saturday_earnings = saturday_attendees * class_price
    sunday_earnings = sunday_attendees * class_price
    total_earnings = saturday_earnings + sunday_earnings
    result = total_earnings
    return result

print(solution())