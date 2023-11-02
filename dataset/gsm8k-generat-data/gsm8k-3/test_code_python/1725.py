def solution():
    """Mike has to get an x-ray and an MRI.  The x-ray is $250 and the MRI is triple that cost.  Insurance covers 80%.  How much did he pay?"""
    # Define the cost of the x-ray and MRI
    XRAY_COST = 250
    MRI_COST = XRAY_COST * 3

    # Calculate the total cost of both procedures
    total_cost = XRAY_COST + MRI_COST

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.8

    # Calculate the amount Mike has to pay
    amount_paid = total_cost - insurance_coverage

    # Display the amount Mike has to pay
    result = amount_paid
    return result

print(solution())