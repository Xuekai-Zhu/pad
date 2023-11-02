def solution():
     """Studying for her test, Mitchell had read ten chapters of a book before 4 o'clock. When it clocked 4, Mitchell had read 20 pages of the 11th chapter of the book she was studying from. After 4 o'clock, she didn't read the remaining pages of chapter eleven but proceeded and read 2 more chapters of the book. If each chapter in the book had 40 pages, calculate the total number of pages that Mitchell had read altogether?"""
     total_chapters_read = 10 + 1 + 2
     pages_read_in_chapter_eleven = 20
     total_pages_read = (total_chapters_read * 40) - (40 - pages_read_in_chapter_eleven)
     result = total_pages_read
     return result

print(solution())