def solution():
    
    # Define the total number of pages Solo has to read
    total_pages = 4 + 20 + 7 + 8

    # Define the number of days Solo has to read all the pages
    days_left = 4 - 4

    # Calculate the average number of pages Solo needs to read per day
    avg_pages_per_day = total_pages / days_left

    # Display the average number of pages Solo needs to read per day
    result = avg_pages_per_day
    return result

print(solution())