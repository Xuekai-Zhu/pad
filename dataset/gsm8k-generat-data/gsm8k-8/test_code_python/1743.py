def solution():
    # Define the number of shrimp per guest and number of guests
    shrimp_per_guest = 5
    num_guests = 40

    # Calculate the total number of shrimp needed
    total_shrimp = shrimp_per_guest * num_guests

    # Calculate the number of pounds of shrimp needed
    pounds_of_shrimp = total_shrimp / 20

    # Calculate the total cost of the shrimp
    shrimp_cost = pounds_of_shrimp * 17

    result = shrimp_cost
    return result

print(solution())