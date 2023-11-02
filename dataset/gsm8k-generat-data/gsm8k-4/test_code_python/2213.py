def solution():
    """Nancy agreed to pay 40% of the cost of her daughter's car insurance, which costs $80 a month. How much will Nancy pay each year?"""
    # Define the cost of the car insurance and Nancy's contribution percentage
    insurance_cost = 80
    nancy_contribution = 0.4

    # Calculate Nancy's monthly payment
    nancy_payment = insurance_cost * nancy_contribution

    # Calculate Nancy's yearly payment
    yearly_payment = nancy_payment * 12

    result = yearly_payment
    return result

print(solution())