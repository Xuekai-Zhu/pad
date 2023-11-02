def solution():
    first_half_days = 183
    second_half_days = 182
    first_half_miles = 30
    second_half_miles = 35
    
    # Calculate the total miles for the first half of the year
    total_first_half_miles = first_half_days * first_half_miles
    
    # Calculate the total miles for the second half of the year
    total_second_half_miles = second_half_days * second_half_miles
    
    # Calculate the total miles for the entire year
    total_miles = total_first_half_miles + total_second_half_miles
    result = total_miles
    return result

print(solution())