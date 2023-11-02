def solution():
    """Nico borrows 3 books from the library on Monday.  On Monday, he reads the first book with a total of 20 pages.  
    On Tuesday, he reads the second book with a total of 12 pages.  On Wednesday, he reads the third book.  
    If he has read a total of 51 pages from Monday to Wednesday, how many pages did he read on Wednesday?"""
    
    # Define the number of pages read on Monday and Tuesday
    monday_pages = 20
    tuesday_pages = 12
    
    # Calculate the total number of pages read on Monday and Tuesday
    total_pages = monday_pages + tuesday_pages
    
    # Calculate the number of pages Nico read on Wednesday
    wednesday_pages = 51 - total_pages
    
    # Display the number of pages Nico read on Wednesday
    result = wednesday_pages
    return result

print(solution())