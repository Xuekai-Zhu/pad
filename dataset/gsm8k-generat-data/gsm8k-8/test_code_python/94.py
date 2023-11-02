def solution():
    # Define the number of pages John writes in a day and the total number of pages to write
    pages_per_day = 20
    total_pages = 3 * 400
    
    # Calculate the number of days it will take to write the books
    days_to_write = total_pages / pages_per_day
    result = days_to_write
    return result

print(solution())