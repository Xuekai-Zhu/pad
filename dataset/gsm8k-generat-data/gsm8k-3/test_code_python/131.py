def solution():
    """Studying for her test, Mitchell had read ten chapters of a book before 4 o'clock. When it clocked 4, Mitchell had read 20 pages of the 11th chapter of the book she was studying from. After 4 o'clock, she didn't read the remaining pages of chapter eleven but proceeded and read 2 more chapters of the book. If each chapter in the book had 40 pages, calculate the total number of pages that Mitchell had read altogether?"""
    # Define the number of chapters and pages per chapter
    NUM_CHAPTERS = 12
    PAGES_PER_CHAPTER = 40

    # Calculate the number of pages Mitchell had read before 4 o'clock
    pages_before_4 = 10 * PAGES_PER_CHAPTER

    # Calculate the number of pages Mitchell had read of the 11th chapter
    pages_in_11th_chapter = 20

    # Calculate the number of pages Mitchell had read after 4 o'clock
    pages_after_4 = 2 * PAGES_PER_CHAPTER

    # Calculate the total number of pages Mitchell had read
    total_pages = pages_before_4 + pages_in_11th_chapter + pages_after_4

    # Return the result
    result = total_pages
    return result

print(solution())