def solution():
    """Tom's cat needs an expensive surgery. He has had pet insurance for 24 months that cost $20 per month. The procedure cost $5000 but the insurance covers all but 20% of this. How much money did he save by having insurance?"""
    # Define the monthly cost of pet insurance and the duration of coverage in months
    INSURANCE_COST_PER_MONTH = 20
    INSURANCE_DURATION_IN_MONTHS = 24

    # Define the cost of the surgery and the insurance coverage percentage
    SURGERY_COST = 5000
    INSURANCE_COVERAGE_PERCENTAGE = 0.8

    # Calculate the total cost of insurance over the coverage period
    total_insurance_cost = INSURANCE_COST_PER_MONTH * INSURANCE_DURATION_IN_MONTHS

    # Calculate the out-of-pocket cost for the surgery with insurance coverage
    surgery_cost_with_coverage = SURGERY_COST * (1 - INSURANCE_COVERAGE_PERCENTAGE)

    # Calculate the total amount saved with insurance coverage
    amount_saved_with_insurance = SURGERY_COST - surgery_cost_with_coverage - total_insurance_cost

    # Return the result
    result = amount_saved_with_insurance
    return result

print(solution())