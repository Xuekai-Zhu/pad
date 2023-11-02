def solution():
    """Rita is reading a five-chapter book with 95 pages. Each chapter has three pages more than the previous one. How many pages does the first chapter have?"""
    # Define the total number of chapters and pages
    total_chapters = 5
    total_pages = 95

    # Calculate the difference in number of pages between consecutive chapters
    page_difference = 3

    # Calculate the sum of the page numbers in all the chapters
    # Using the formula for sum of an arithmetic series
    # Sn = n/2(2*a + (n-1)*d)
    # where n is the number of terms, a is the first term, and d is the common difference
    sum_pages = (total_chapters / 2) * (2 * 1 + (total_chapters - 1) * page_difference)

    # Calculate the number of pages in the first chapter
    first_chapter_pages = sum_pages - (total_pages - 1)

    # return the result
    result = first_chapter_pages
    return result

print(solution())