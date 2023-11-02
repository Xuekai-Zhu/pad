def solution():
    """A school is adding 5 rows of seats to the auditorium. Each row has 8 seats and each seat costs $30. A parent, being a seat manufacturer, offered a 10% discount on each group of 10 seats purchased. How much will the school pay for the new seats?"""
    # Define the number of rows, seats per row, and seat cost
    num_rows = 5
    seats_per_row = 8
    seat_cost = 30

    # Calculate the total number of seats
    total_seats = num_rows * seats_per_row

    # Calculate the total cost of the seats before discount
    cost_before_discount = total_seats * seat_cost

    # Calculate the number of seat groups (groups of 10 seats)
    num_seat_groups = total_seats // 10

    # Calculate the total cost savings from the discount
    cost_savings = num_seat_groups * (10 * seat_cost * 0.1)

    # Calculate the total cost of the seats after discount
    cost_after_discount = cost_before_discount - cost_savings

    result = cost_after_discount
    return result

print(solution())