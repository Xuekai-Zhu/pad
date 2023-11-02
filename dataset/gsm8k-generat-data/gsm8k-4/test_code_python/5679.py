def solution():
    """Kelly puts string cheeses in her kids lunches 5 days per week. Her oldest wants 2 every day and her youngest will only eat 1. The packages come with 30 string cheeses per pack. How many packages of string cheese will Kelly need to fill her kids lunches for 4 weeks?"""
    
    # Define the number of days in a week, the number of weeks, and the number of string cheeses per package
    DAYS_PER_WEEK = 5
    WEEKS = 4
    STRING_CHEESES_PER_PACK = 30
    
    # Define the number of string cheeses needed for each child per week
    CHEESES_PER_WEEK = 2 + 1
    
    # Calculate the total number of string cheeses needed for both children for the entire month
    total_cheeses = CHEESES_PER_WEEK * DAYS_PER_WEEK * WEEKS
    
    # Calculate the number of packages needed
    packages_needed = total_cheeses / STRING_CHEESES_PER_PACK
    
    # Round up to the nearest integer to account for partial packages needed
    packages_needed = int(-(-packages_needed // 1))
    
    result = packages_needed
    return result

print(solution())