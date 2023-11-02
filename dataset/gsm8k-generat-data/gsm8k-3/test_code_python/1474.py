def solution():
    """Evelyn’s family watched 10 hours of television last week. 
    The week before, they watched 8 hours of television. 
    If they watch 12 hours of television next week, 
    what is the average number of hours of television that they watch per week?"""
    
    # Define the total number of hours watched over three weeks
    total_hours = 10 + 8 + 12
    
    # Calculate the average number of hours per week
    average_hours = total_hours / 3
    
    # Display the average number of hours
    result = average_hours
    return result

print(solution())