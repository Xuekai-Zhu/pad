def solution():
    """A charcoal grill burns fifteen coals to ash every twenty minutes of grilling. The grill ran for long enough to burn three bags of coals. Each bag of coal contains 60 coals. How long did the grill run?"""
    
    # Define the number of coals burned per 20-minute interval
    coals_burned = 15
    
    # Define the number of coals per bag
    coals_per_bag = 60
    
    # Calculate the total number of coals burned
    total_coals = 3 * coals_per_bag
    
    # Calculate the number of 20-minute intervals needed to burn all the coals
    intervals = total_coals / coals_burned
    
    # Convert the intervals to hours
    hours = intervals / 3
    
    # Convert the decimal portion of the hours to minutes
    minutes = int((hours % 1) * 60)
    
    # Convert the remaining hours to whole hours
    hours = int(hours)
    
    # Format the result as a string
    result = "{} hours, {} minutes".format(hours, minutes)
    return result

print(solution())