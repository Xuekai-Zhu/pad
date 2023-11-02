def solution():
    """Wendy went to the dentist for a cleaning, two fillings, and a tooth extraction.
    The dentist charges $70 for a cleaning and $120 for a filling. Wendy’s dentist bill was five times the cost of a filling.
    What did Wendy pay for the tooth extraction?"""
    cleaning_cost = 70
    filling_cost = 120
    total_fillings_cost = 2 * filling_cost
    total_bill = 5 * filling_cost + cleaning_cost + total_fillings_cost + x
    # x represents the cost of tooth extraction

    # Simplifying the equation
    x = total_bill - cleaning_cost - total_fillings_cost - 5 * filling_cost
    result = x
    return result

print(solution())