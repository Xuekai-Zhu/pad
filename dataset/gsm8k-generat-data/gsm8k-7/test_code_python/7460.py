def solution():
    num_rows = 5
    seats_per_row = 8
    seat_cost = 30
    discount = 0.1
    group_size = 10

    # Calculate the total number of seats being added
    total_seats = num_rows * seats_per_row

    # Calculate the total cost of all seats before discount
    total_cost = total_seats * seat_cost

    # Calculate the number of groups of seats
    num_groups = total_seats // group_size

    # Calculate the total discount
    total_discount = num_groups * group_size * seat_cost * discount

    # Calculate the final cost after discount
    final_cost = total_cost - total_discount
    result = final_cost
    return result

print(solution())