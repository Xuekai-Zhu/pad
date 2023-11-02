def solution():
    """A person borrowed an amount of money for a year at an interest rate of 12%. If the total interest is $1500, what was the original borrowed amount?"""
    # Define the interest rate and total interest
    INTEREST_RATE = 0.12
    TOTAL_INTEREST = 1500

    # Calculate the borrowed amount
    borrowed_amount = TOTAL_INTEREST / INTEREST_RATE

    # Display the borrowed amount
    result = borrowed_amount
    return result

print(solution())