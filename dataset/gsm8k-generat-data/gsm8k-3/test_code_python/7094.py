def solution(): 
    """Molly got a bike for her thirteenth birthday. She rode her bike 3 miles a day, every day, until she turned 16. How many miles did Molly ride on her bike?"""
    
    # Define the number of years Molly rode her bike
    years_riding = 16 - 13
    
    # Define the number of miles Molly rode per day
    miles_per_day = 3
    
    # Calculate the total number of miles Molly rode
    total_miles = years_riding * 365 * miles_per_day
    
    # Display the total number of miles
    result = total_miles
    return result

print(solution())