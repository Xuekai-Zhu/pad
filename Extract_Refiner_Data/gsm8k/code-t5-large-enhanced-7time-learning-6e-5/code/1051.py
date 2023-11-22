def solution():
    
    # Define the cost of normal insurance per month
    NORMAL_COST = 120

    # Calculate the cost of insurance per month
    INSURANCE_COST = NORMAL_COST * 1.6

    # Calculate the cost of insurance per year
    INSURANCE_COST_YEAR = INSURANCE_COST * 12

    # Display the cost of insurance per year
    result = INSURANCE_COST_YEAR
    return result

print(solution())