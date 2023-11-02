def solution():
    """John gets a new EpiPen every 6 months. They cost $500 and insurance covers 75%. How much does he pay per year?"""
    # Define the cost of an EpiPen and insurance coverage
    EPIDPEN_COST = 500
    INSURANCE_COVERAGE = 0.75

    # Calculate the annual cost of EpiPens
    num_epipens = 2 # John gets a new EpiPen every 6 months, so 2 per year
    total_cost = num_epipens * EPIDPEN_COST
    out_of_pocket_cost = total_cost * (1 - INSURANCE_COVERAGE)
    
    # Display John's out-of-pocket cost per year
    result = out_of_pocket_cost
    return result

print(solution())