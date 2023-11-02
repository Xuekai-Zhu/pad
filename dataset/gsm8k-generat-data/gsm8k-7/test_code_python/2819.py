def solution():
    book1_chapters = 20
    book2_chapters = 15
    book3_chapters = book2_chapters * 2
    book4_chapters = (book1_chapters + book2_chapters + book3_chapters) / 2

    total_chapters = book1_chapters + (book2_chapters * 2) + book4_chapters

    result = total_chapters
    return result

print(solution())