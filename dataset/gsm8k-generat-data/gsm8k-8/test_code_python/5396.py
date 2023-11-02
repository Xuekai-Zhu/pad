def solution():
    # Define the minimum required pages to pass the class
    target_pages = 100
    
    # Define the number of pages read on the first day
    first_day_pages = 10
    
    # Calculate the number of pages Justin will need to read in the remaining 6 days
    remaining_days = 6
    remaining_pages = target_pages - first_day_pages
    pages_per_day = remaining_pages / (2 ** remaining_days - 1)
    
    # Calculate the total number of pages Justin will have read after the week is over
    total_pages = first_day_pages + remaining_pages + pages_per_day
    
    result = total_pages
    return result

print(solution())