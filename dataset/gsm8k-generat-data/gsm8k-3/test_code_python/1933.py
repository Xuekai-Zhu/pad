def solution():
    """Wendy went to the dentist for a cleaning, two fillings, and a tooth extraction. The dentist charges $70 for a cleaning and $120 for a filling. Wendy's dentist bill was five times the cost of a filling. What did Wendy pay for the tooth extraction?"""
    # Define the cost of a cleaning and a filling
    CLEANING_COST = 70
    FILLING_COST = 120

    # Calculate the cost of two fillings
    fillings_cost = 2 * FILLING_COST

    # Calculate the total cost of the dentist bill
    total_cost = 5 * FILLING_COST + CLEANING_COST + fillings_cost

    # Calculate the cost of the tooth extraction
    extraction_cost = total_cost - (CLEANING_COST + fillings_cost)

    # Display the cost of the tooth extraction
    result = extraction_cost
    return result

print(solution())