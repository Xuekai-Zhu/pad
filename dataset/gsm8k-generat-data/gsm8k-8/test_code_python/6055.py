def solution():
    # Define the number of pages Beatrix read
    beatrix_pages = 704

    # Calculate the number of pages Cristobal read
    cristobal_pages = 15 + 3 * beatrix_pages

    # Calculate the difference in the number of pages read
    page_difference = cristobal_pages - beatrix_pages

    result = page_difference
    return result

print(solution())