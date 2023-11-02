def solution():
    """Brian likes to read books. He read one book that had 20 chapters, two books that had 15 chapters each, and one book that had half the chapters of the three previous books put together. How many chapters of books did Brian read?"""
    book1_chapters = 20
    book2_chapters = 15
    book3_chapters = 0.5 * (book1_chapters + 2 * book2_chapters)
    total_chapters = book1_chapters + 2* book2_chapters + book3_chapters
    result = total_chapters
    return result

print(solution())