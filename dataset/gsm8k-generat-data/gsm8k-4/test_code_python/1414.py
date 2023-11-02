def solution():
    """Stacy just bought a 6 month prescription of flea & tick medicine for her dog for $150.00 online.  Her cashback app was offering 10% cashback and she has a mail-in rebate for $25.00 on a 6-month prescription.  How much will the medicine cost after cash back and rebate offers?"""
    # Define the initial cost of the medicine
    initial_cost = 150

    # Calculate the cashback amount
    cashback_amount = initial_cost * 0.1

    # Calculate the cost after cashback
    cost_after_cashback = initial_cost - cashback_amount

    # Calculate the cost after rebate
    cost_after_rebate = cost_after_cashback - 25

    # Return the result
    result = cost_after_rebate
    return result

print(solution())