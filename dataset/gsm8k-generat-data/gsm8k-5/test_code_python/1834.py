def solution():
    # Calculate the cost of lodging for the first 3 days
    hostel_cost = 15 * 3

    # Calculate the cost of lodging for the 4th and 5th days
    cabin_cost = 45 / 3  # Jimmy shares the cost with 2 friends, so they pay $15 each per night
    cabin_total_cost = cabin_cost * 2

    # Calculate the total cost of lodging
    total_cost = hostel_cost + cabin_total_cost
    result = total_cost
    return result

print(solution())