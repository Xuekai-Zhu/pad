def solution():
    shrimp_per_guest = 5
    num_guests = 40
    cost_per_pound = 17.0
    shrimp_per_pound = 20

    # Calculate the total number of shrimp needed
    total_shrimp = shrimp_per_guest * num_guests

    # Calculate the total pounds of shrimp needed
    total_pounds = total_shrimp / shrimp_per_pound

    # Calculate the total cost of all shrimp needed
    total_cost = total_pounds * cost_per_pound
    result = total_cost
    return result

print(solution())