def solution():
    """Studying for her test, Mitchell had read ten chapters of a book before 4 o'clock. When it clocked 4, Mitchell had read 20 pages of the 11th chapter of the book she was studying from. After 4 o'clock, she didn't read the remaining pages of chapter eleven but proceeded and read 2 more chapters of the book. If each chapter in the book had 40 pages, calculate the total number of pages that Mitchell had read altogether?"""
    # Define the number of pages per chapter and the number of chapters already read
    PAGES_PER_CHAPTER = 40
    CHAPTERS_READ_BEFORE_4 = 10

    # Define the number of pages read from chapter 11 and the number of chapters read after 4
    PAGES_READ_IN_CHAPTER_11 = 20
    CHAPTERS_READ_AFTER_4 = 2

    # Calculate the total number of chapters read
    total_chapters_read = CHAPTERS_READ_BEFORE_4 + CHAPTERS_READ_AFTER_4 + 1

    # Calculate the total number of pages read
    total_pages_read = (CHAPTERS_READ_BEFORE_4 + 1) * PAGES_PER_CHAPTER + PAGES_READ_IN_CHAPTER_11 + CHAPTERS_READ_AFTER_4 * PAGES_PER_CHAPTER

    # Return the result
    result = total_pages_read
    return result

print(solution())