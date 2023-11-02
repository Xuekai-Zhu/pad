def solution():
    """John gets a new EpiPen every 6 months. They cost $500 and insurance covers 75%. How much does he pay per year?"""
    # Define the cost of one EpiPen and the insurance coverage
    EPIPEN_COST = 500
    INSURANCE_COVERAGE = 0.75

    # Calculate the out-of-pocket cost for each EpiPen
    out_of_pocket_cost = EPIPEN_COST * (1 - INSURANCE_COVERAGE)

    # Calculate the total out-of-pocket cost for one year
    total_cost_per_year = out_of_pocket_cost * 2

    # Return the result
    result = total_cost_per_year
    return result

print(solution())