def solution():
    """An investment bank gives 10 percent interest at the end of every month. How much money in total will you have, including interest, at the end of 2 months if you invest $300?"""
    # Define the initial investment amount and the monthly interest rate
    INITIAL_AMOUNT = 300
    MONTHLY_INTEREST_RATE = 0.1

    # Calculate the interest earned in the first month and add it to the initial amount
    interest_1 = INITIAL_AMOUNT * MONTHLY_INTEREST_RATE
    total_1 = INITIAL_AMOUNT + interest_1

    # Calculate the interest earned in the second month and add it to the total from the first month
    interest_2 = total_1 * MONTHLY_INTEREST_RATE
    total_2 = total_1 + interest_2

    # Calculate the total amount at the end of 2 months
    total_amount = total_2

    # Display the total amount
    result = total_amount
    return result

print(solution())