def solution():
    """Nancy agreed to pay 40% of the cost of her daughter's car insurance, which costs $80 a month. How much will Nancy pay each year?"""
    # Define the cost of the car insurance per month and the percentage Nancy agreed to pay
    INSURANCE_COST = 80
    NANCY_PERCENTAGE = 0.4

    # Calculate Nancy's monthly payment
    nancy_payment = INSURANCE_COST * NANCY_PERCENTAGE

    # Calculate Nancy's yearly payment
    yearly_payment = nancy_payment * 12

    # Display Nancy's yearly payment
    result = yearly_payment
    return result

print(solution())