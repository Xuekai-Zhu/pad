def solution():
    """Cora started reading a 158-page book on Monday, and she decided she wanted to finish it by the end of Friday. She read 23 pages on Monday, 38 pages on Tuesday, and 61 pages on Wednesday. She knows she will have time to read twice as much on Friday as she does on Thursday. How many pages does she have to read on Thursday to finish the book in time?"""
    # Define the number of pages already read
    pages_read = 23 + 38 + 61

    # Define the number of pages Cora needs to read on Friday
    friday_pages = 2 * thursday_pages

    # Define the total number of pages Cora needs to read to finish the book in time
    total_pages = 158 - pages_read

    # Calculate the number of pages Cora needs to read on Thursday
    thursday_pages = (total_pages - friday_pages) / 2

    # Display the number of pages Cora needs to read on Thursday
    result = thursday_pages
    return result

print(solution())