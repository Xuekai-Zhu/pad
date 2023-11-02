def solution():
    adult_count = 12 - 2  # Total number of adults in Hans's party
    child_count = 2  # Total number of children in Hans's party
    deposit_per_adult = 3  # Deposit per adult is $3
    deposit_per_child = 1  # Deposit per child is $1
    flat_deposit = 20  # Flat deposit is $20

    # Calculate the total deposit for adults
    adult_deposit = adult_count * deposit_per_adult

    # Calculate the total deposit for children
    child_deposit = child_count * deposit_per_child

    # Add up all the deposits
    total_deposit = adult_deposit + child_deposit + flat_deposit
    result = total_deposit
    return result

print(solution())