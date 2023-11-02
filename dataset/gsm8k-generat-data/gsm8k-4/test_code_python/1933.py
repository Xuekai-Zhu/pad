def solution():
    """Wendy went to the dentist for a cleaning, two fillings, and a tooth extraction. The dentist charges $70 for a cleaning and $120 for a filling. Wendy’s dentist bill was five times the cost of a filling. What did Wendy pay for the tooth extraction?"""
    # Define the cost of a filling and the number of fillings Wendy had
    filling_cost = 120
    num_fillings = 2

    # Calculate the cost of the cleaning and the fillings
    cleaning_cost = 70
    fillings_cost = filling_cost * num_fillings

    # Calculate the total cost of the dental work
    total_cost = 5 * filling_cost

    # Calculate the cost of the tooth extraction
    extraction_cost = total_cost - cleaning_cost - fillings_cost

    # return the result
    result = extraction_cost
    return result

print(solution())