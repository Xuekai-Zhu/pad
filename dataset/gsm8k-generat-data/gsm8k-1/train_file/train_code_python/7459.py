def solution():
    """A school is adding 5 rows of seats to the auditorium. Each row has 8 seats and each seat costs $30. A parent, being a seat manufacturer, offered a 10% discount on each group of 10 seats purchased. How much will the school pay for the new seats?"""
    rows_added = 5
    seats_per_row = 8
    seat_cost = 30
    total_seats = rows_added * seats_per_row
    total_cost = total_seats * seat_cost
    
    if total_seats % 10 == 0:
        num_groups = total_seats // 10
    else:
        num_groups = total_seats // 10 + 1
        
    discount = num_groups * (seat_cost * 10 * 0.1)
    total_cost -= discount
    
    result = total_cost
    return result

print(solution())