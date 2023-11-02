def solution():
    """Sabina is starting her first year of college that costs $30,000. She has saved $10,000 for her first year. She was awarded a grant that will cover 40% of the remainder of her tuition. How much will Sabina need to apply for to receive a loan that will cover her tuition?"""
    # Define the cost of tuition and the amount Sabina has saved
    TUITION_COST = 30000
    SAVED_AMOUNT = 10000

    # Calculate the amount of tuition remaining after savings
    remaining_tuition = TUITION_COST - SAVED_AMOUNT

    # Calculate the amount of tuition covered by the grant
    grant_amount = remaining_tuition * 0.4

    # Calculate the total amount of tuition for which Sabina will need a loan
    loan_amount = remaining_tuition - grant_amount

    # Display the required loan amount
    result = loan_amount
    return result

print(solution())