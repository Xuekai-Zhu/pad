def solution():
    """Cristobal read 15 more than three times the pages that Beatrix read. If Beatrix read 704 pages, how many more pages did Cristobal read?"""
    # Define the number of pages Beatrix read
    beatrix_pages = 704

    # Calculate the number of pages Cristobal read
    cristobal_pages = 3 * beatrix_pages + 15

    # Calculate how many more pages Cristobal read
    more_pages = cristobal_pages - beatrix_pages

    # Display how many more pages Cristobal read
    result = more_pages
    return result

print(solution())