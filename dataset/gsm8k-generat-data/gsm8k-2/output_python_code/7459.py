def solution():
    """A school is adding 5 rows of seats to the auditorium. Each row has 8 seats and each seat costs $30. A parent, being a seat manufacturer, offered a 10% discount on each group of 10 seats purchased. How much will the school pay for the new seats?"""
    num_rows = 5
    seats_per_row = 8
    seat_cost = 30
    total_seats = num_rows * seats_per_row
    subtotal = total_seats * seat_cost
    discount_groups = total_seats // 10
    discounted_seats = discount_groups * 10
    discounted_cost = subtotal / 10
    total_cost = subtotal - discounted_cost
    result = total_cost
    return result

print(solution())