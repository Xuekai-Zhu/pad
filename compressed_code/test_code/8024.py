def solution():
    
    book_1_chapters = 20
    book_2_chapters = 15
    book_3_chapters = (book_1_chapters + (2 * book_2_chapters)) / 2
    total_chapters = book_1_chapters + (2 * book_2_chapters) + book_3_chapters
    result = total_chapters
    return result

print(solution())