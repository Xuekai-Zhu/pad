def solution():
    # Calculate the cost of one filling
    cost_filling = 120
    
    # Calculate the cost of the cleaning and two fillings
    cost_cleaning_and_fillings = 70 + (2 * cost_filling)
    
    # Calculate the total cost of the bill
    total_cost = 5 * cost_filling + cost_cleaning_and_fillings
    
    # Subtract the cost of the cleaning and fillings to get the cost of the tooth extraction
    cost_tooth_extraction = total_cost - cost_cleaning_and_fillings
    
    result = cost_tooth_extraction
    return result

print(solution())