def solution():
    """Molly got a bike for her thirteenth birthday. She rode her bike 3 miles a day, every day, until she turned 16. How many miles did Molly ride on her bike?"""
    # Define the number of years Molly rode her bike
    years_riding = 16 - 13

    # Calculate the total number of days Molly rode her bike
    days_riding = years_riding * 365

    # Calculate the total number of miles Molly rode her bike
    miles_riding = days_riding * 3

    # return the result
    result = miles_riding
    return result

print(solution())