def solution():
    # Define the total number of pages and pages read so far
    total_pages = 100
    pages_read = 35 + (35 - 5)
    
    # Define the number of pages left to read
    pages_left = total_pages - pages_read
    
    # Define the number of days left to finish the book
    days_left = 3 - 2
    
    # Calculate the number of pages he needs to read each day to finish the book
    pages_per_day = pages_left / days_left
    
    # Calculate the number of pages Lance should read tomorrow
    pages_tomorrow = pages_per_day
    
    result = pages_tomorrow
    return result

print(solution())