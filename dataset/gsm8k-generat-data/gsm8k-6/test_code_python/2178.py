def solution():
    # Calculate the value of the lawnmower after 6 months
    initial_value = 100  
    depreciation_6_months = 0.25 * initial_value  
    value_after_6_months = initial_value - depreciation_6_months  

    # Calculate the value of the lawnmower after 1 year
    depreciation_1_year = 0.20 * value_after_6_months  
    value_after_1_year = value_after_6_months - depreciation_1_year  

    result = value_after_1_year
    return result

print(solution())