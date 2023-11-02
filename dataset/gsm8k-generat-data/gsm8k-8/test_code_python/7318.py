def solution():
    # Define the number of pages in each book
    purple_pages = 230
    orange_pages = 510

    # Calculate the total number of pages Mirella read
    purple_total_pages = purple_pages * 5
    orange_total_pages = orange_pages * 4
    total_pages = purple_total_pages + orange_total_pages
    
    # Calculate the difference between orange and purple pages
    orange_pages_read = orange_total_pages - purple_total_pages
    
    result = orange_pages_read
    return result

print(solution())