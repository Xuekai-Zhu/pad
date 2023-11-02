def solution():
    """Rita is reading a five-chapter book with 95 pages. Each chapter has three pages more than the previous one. How many pages does the first chapter have?"""
    # Set up variables
    total_pages = 95
    current_chapter = 1
    current_page = 0

    # Loop through each chapter
    while current_chapter <= 5:
        # Calculate the number of pages in the current chapter
        current_page += 3
        # Add the current page count to the total page count
        total_pages -= current_page
        # Increment the current chapter
        current_chapter += 1

    # Calculate the number of pages in the first chapter
    first_chapter_pages = total_pages + 3

    # Display the number of pages in the first chapter
    result = first_chapter_pages
    return result

print(solution())