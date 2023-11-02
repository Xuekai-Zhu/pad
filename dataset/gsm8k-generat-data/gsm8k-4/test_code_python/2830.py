def solution():
    """Derek puts $2 away in January, $4 away in February, $8 away in March, $16 away in April and follows this savings pattern through to December. How much money does he have to spare and save by December?"""
    # Define the initial savings and amount to be doubled each month
    savings = 2
    doubling_amount = 2

    # Add the doubled amount to savings each month
    for i in range(1, 12):
        savings += doubling_amount
        doubling_amount *= 2

    # Return the total savings
    result = savings
    return result

print(solution())