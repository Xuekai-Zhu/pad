def solution():
    """Rob planned on spending three hours reading in preparation for his literature exam. If he ends up spending only three-quarters of this time reading, and he reads a page every fifteen minutes, how many pages did he read in this time?"""
    
    # Convert 3 hours to minutes
    total_time = 3 * 60
    
    # Calculate the actual reading time
    actual_time = total_time * 0.75
    
    # Calculate the number of pages read
    pages_read = actual_time / 15
    
    # Display the number of pages read
    result = pages_read
    return result

print(solution())