def solution():
    """The novel that everyone is reading for English class has half as many pages as their history book.  Their science book has 4 times the amount of pages as their novel.  If the history book has 300 pages, how many pages does their science book have?"""
    # Define the number of pages in the history book
    history_pages = 300

    # Calculate the number of pages in the novel
    novel_pages = history_pages / 2

    # Calculate the number of pages in the science book
    science_pages = novel_pages * 4

    # Display the number of pages in the science book
    result = science_pages
    return result

print(solution())