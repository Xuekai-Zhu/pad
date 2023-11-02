def solution():
    # Define the number of rows and seats per row
    num_rows = 5
    seats_per_row = 8

    # Calculate the total number of seats
    total_seats = num_rows * seats_per_row

    # Calculate the total cost of the seats without discount
    seat_cost = 30
    total_cost = total_seats * seat_cost

    # Calculate the number of groups of 10 seats
    num_groups = total_seats // 10

    # Calculate the total discount amount
    discount = 0.1 * seat_cost * 10 * num_groups

    # Calculate the final cost with discount
    final_cost = total_cost - discount

    result = final_cost
    return result

print(solution())