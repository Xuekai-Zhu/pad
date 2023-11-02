def solution():
    """Brian likes to read books. He read one book that had 20 chapters, two books that had 15 chapters each, and one book that had half the chapters of the three previous books put together. How many chapters of books did Brian read?"""
    book_1_chapters = 20
    book_2_chapters = 15
    book_3_chapters = (book_1_chapters + (2 * book_2_chapters)) / 2
    total_chapters = book_1_chapters + (2 * book_2_chapters) + book_3_chapters
    result = total_chapters
    return result

print(solution())