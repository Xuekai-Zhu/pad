def solution():
    """A school is adding 5 rows of seats to the auditorium. Each row has 8 seats and each seat costs $30. A parent, being a seat manufacturer, offered a 10% discount on each group of 10 seats purchased. How much will the school pay for the new seats?"""
    # Define the number of rows and seats per row
    rows = 5
    seats_per_row = 8

    # Define the cost per seat and the discount rate
    seat_cost = 30
    discount_rate = 0.1

    # Calculate the total number of seats and groups of 10 seats
    total_seats = rows * seats_per_row
    groups_of_10 = total_seats // 10

    # Calculate the total cost of groups of 10 seats and the remaining seats
    group_cost = groups_of_10 * 10 * seat_cost * (1 - discount_rate)
    remaining_seats = total_seats % 10
    remaining_cost = remaining_seats * seat_cost

    # Calculate the total cost of all the seats
    total_cost = group_cost + remaining_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())