def solution():
    """Studying for her test, Mitchell had read ten chapters of a book before 4 o'clock. When it clocked 4, Mitchell had read 20 pages of the 11th chapter of the book she was studying from. After 4 o'clock, she didn't read the remaining pages of chapter eleven but proceeded and read 2 more chapters of the book. If each chapter in the book had 40 pages, calculate the total number of pages that Mitchell had read altogether?"""
    chapters_before_4_oclock = 10
    pages_read_in_chapter_11 = 20
    chapters_after_4_oclock = 2
    total_chapters_read = chapters_before_4_oclock + chapters_after_4_oclock
    total_pages_read = (chapters_before_4_oclock + chapters_after_4_oclock) * 40 - pages_read_in_chapter_11
    result = total_pages_read
    return result

print(solution())