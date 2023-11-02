def solution():
    """Sabina is starting her first year of college that costs $30,000. She has saved $10,000 for her first year. She was awarded a grant that will cover 40% of the remainder of her tuition. How much will Sabina need to apply for to receive a loan that will cover her tuition?"""
    # Define the total cost of tuition and the amount saved by Sabina
    tuition_cost = 30000
    savings = 10000

    # Calculate the remaining tuition cost after the savings
    remaining_cost = tuition_cost - savings

    # Calculate the amount covered by the grant
    grant_amount = remaining_cost * 0.4

    # Calculate the amount needed to apply for a loan
    loan_amount = remaining_cost - grant_amount

    # Display the result
    result = loan_amount
    return result

print(solution())