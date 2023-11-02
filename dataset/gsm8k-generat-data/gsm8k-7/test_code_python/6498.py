def solution():
    summer_length = 80
    deshaun_books = 60
    pages_per_book = 320
    closest_percent = 0.75
    
    # Calculate the total number of pages DeShaun read
    deshaun_pages = deshaun_books * pages_per_book
    
    # Calculate the total number of pages the second person read
    closest_pages = deshaun_pages * closest_percent
    
    # Calculate the average number of pages read per day by the second person
    avg_pages_per_day = closest_pages / summer_length
    result = avg_pages_per_day
    return result

print(solution())