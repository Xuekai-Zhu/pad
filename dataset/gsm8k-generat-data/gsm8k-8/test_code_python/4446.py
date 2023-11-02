def solution():
    # Define the number of adults and children in the party
    adults = 12 - 2
    children = 2

    # Calculate the deposit for the adults and children separately
    adult_deposit = 3 * adults
    child_deposit = 1 * children

    # Calculate the total deposit
    total_deposit = 20 + adult_deposit + child_deposit
    result = total_deposit
    return result

print(solution())