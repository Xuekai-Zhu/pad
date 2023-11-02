def solution():
    """Mr. and Mrs. McPherson have to renew their rent by the end of the year. They agreed that Mrs. McPherson would raise 30% of the money. If their rent is $1200 per year, how much does Mr. McPherson need to raise to complete the rent?"""
    # Define the rent amount and the percentage Mrs. McPherson will raise
    RENT_AMOUNT = 1200
    PERCENTAGE_RAISED_BY_MRS = 0.3

    # Calculate the amount raised by Mrs. McPherson
    amount_raised_by_mrs = RENT_AMOUNT * PERCENTAGE_RAISED_BY_MRS

    # Calculate the amount Mr. McPherson needs to raise
    amount_to_raise_by_mr = RENT_AMOUNT - amount_raised_by_mrs

    # Display the amount Mr. McPherson needs to raise
    result = amount_to_raise_by_mr
    return result

print(solution())