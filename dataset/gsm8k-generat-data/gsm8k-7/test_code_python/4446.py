def solution():
    num_adults = 10     # Subtract 2 for the children
    num_children = 2
    deposit_per_adult = 3
    deposit_per_child = 1
    flat_deposit = 20

    # Calculate the total deposit for all adults
    total_adult_deposit = num_adults * deposit_per_adult

    # Calculate the total deposit for all children
    total_child_deposit = num_children * deposit_per_child

    # Calculate the total deposit for the reservation
    total_deposit = flat_deposit + total_adult_deposit + total_child_deposit
    result = total_deposit
    return result

print(solution())