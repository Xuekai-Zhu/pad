def solution():
    """Stacy just bought a 6 month prescription of flea & tick medicine for her dog for $150.00 online.  Her cashback app was offering 10% cashback and she has a mail-in rebate for $25.00 on a 6-month prescription.  How much will the medicine cost after cash back and rebate offers?"""
    # Define the cost of the medicine
    medicine_cost = 150.00

    # Calculate the cashback amount
    cashback = medicine_cost * 0.1

    # Calculate the total cost after cashback
    total_cost = medicine_cost - cashback

    # Calculate the cost after rebate
    total_cost -= 25.00

    # Display the final cost
    result = total_cost
    return result

print(solution())