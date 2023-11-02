def solution():
    """Tom's cat needs an expensive surgery.  He has had pet insurance for 24 months that cost $20 per month.  The procedure cost $5000 but the insurance covers all but 20% of this.  How much money did he save by having insurance?"""
    # Define the cost of insurance per month and the number of months of coverage
    INSURANCE_COST = 20
    MONTHS_OF_COVERAGE = 24

    # Calculate the total cost of insurance
    insurance_cost = INSURANCE_COST * MONTHS_OF_COVERAGE

    # Calculate the amount that Tom has to pay for the surgery after insurance
    remaining_cost = 5000 * 0.2

    # Calculate the total amount Tom saved with insurance
    total_savings = remaining_cost - insurance_cost

    # Display the total amount saved
    result = total_savings
    return result

print(solution())