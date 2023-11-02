def solution():
    num_pennies = 200
    num_nickels = 100
    num_dimes = 330

    # Convert pennies to dollars
    total_pennies = num_pennies
    total_pennies_in_dollars = total_pennies / 100

    # Convert nickels to dollars
    total_nickels = num_nickels * 5
    total_nickels_in_dollars = total_nickels / 100

    # Convert dimes to dollars
    total_dimes = num_dimes * 10
    total_dimes_in_dollars = total_dimes / 100

    # Calculate the total amount saved by all three kids
    total_saved = total_pennies_in_dollars + total_nickels_in_dollars + total_dimes_in_dollars
    result = total_saved
    return result

print(solution())