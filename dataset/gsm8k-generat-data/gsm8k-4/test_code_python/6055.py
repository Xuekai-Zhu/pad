def solution():
    """Cristobal read 15 more than three times the pages that Beatrix read. If Beatrix read 704 pages, how many more pages did Cristobal read?"""
    # Define the number of pages Beatrix read
    beatrix_pages = 704

    # Calculate the number of pages Cristobal read using the given relationship
    cristobal_pages = 3 * beatrix_pages + 15

    # Calculate the difference in pages read between Cristobal and Beatrix
    page_difference = cristobal_pages - beatrix_pages

    # return the result
    result = page_difference
    return result

print(solution())