def solution():
    venue_cost = 10000
    num_guests = 50
    cost_per_guest = 500
    percent_increase = 0.6

    # Calculate the total cost of the venue and John's desired number of guests
    base_cost = venue_cost + (num_guests * cost_per_guest)

    # Calculate the desired number of guests with the 60% increase
    desired_num_guests = num_guests * (1 + percent_increase)

    # Calculate the total cost with the increased number of guests
    total_cost = base_cost + (desired_num_guests * cost_per_guest)

    result = total_cost
    return result

print(solution())