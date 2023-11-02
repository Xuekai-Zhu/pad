def solution():
    # Calculate the total number of seats and the original cost without discount
    num_rows = 5
    seats_per_row = 8
    num_seats = num_rows * seats_per_row
    seat_cost = 30
    original_cost = num_seats * seat_cost

    # Calculate the number of groups of 10 seats and the cost with discount
    num_groups = num_seats // 10
    cost_per_group = 10 * seat_cost * 0.9
    remaining_seats = num_seats % 10
    remaining_cost = remaining_seats * seat_cost

    # Total cost with discount
    total_cost = num_groups * cost_per_group + remaining_cost
    result = total_cost
    return result

print(solution())