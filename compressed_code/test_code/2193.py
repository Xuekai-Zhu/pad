def solution():
    
    book1_chapters = 20
    book2_chapters = 15
    book3_chapters = 0.5 * (book1_chapters + 2 * book2_chapters)
    total_chapters = book1_chapters + 2* book2_chapters + book3_chapters
    result = total_chapters
    return result

print(solution())