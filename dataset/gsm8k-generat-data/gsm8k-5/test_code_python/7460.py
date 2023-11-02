def solution():
    rows_added = 5  # The school is adding 5 rows of seats
    seats_per_row = 8  # Each row has 8 seats
    seat_cost = 30  # Each seat costs $30
    seats_per_group = 10  # The discount applies to each group of 10 seats

    # Calculate the total cost of the new seats before the discount
    total_seats = rows_added * seats_per_row
    total_cost = total_seats * seat_cost

    # Apply the discount to each group of 10 seats
    groups_of_ten = total_seats // seats_per_group
    total_discount = groups_of_ten * (seats_per_group * seat_cost * 0.1)
    discounted_cost = total_cost - total_discount

    result = discounted_cost
    return result

print(solution())