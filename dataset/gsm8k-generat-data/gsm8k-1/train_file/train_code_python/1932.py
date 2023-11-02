def solution():
    """Wendy went to the dentist for a cleaning, two fillings, and a tooth extraction. The dentist charges $70 for a cleaning and $120 for a filling. Wendy’s dentist bill was five times the cost of a filling. What did Wendy pay for the tooth extraction?"""
    cleaning_cost = 70
    filling_cost = 120
    total_fillings = 2
    total_cost = filling_cost * total_fillings * 5 # 5 times the cost of a filling
    extraction_cost = total_cost - (cleaning_cost + (filling_cost * total_fillings))
    result = extraction_cost
    return result

print(solution())