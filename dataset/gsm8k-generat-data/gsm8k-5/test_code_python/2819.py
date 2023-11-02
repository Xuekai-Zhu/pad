def solution():
    # Total number of chapters in the first book
    book1 = 20

    # Total number of chapters in the two books with 15 chapters each
    book2 = 15 * 2

    # Total number of chapters in the third book that has half the chapters of the three previous books put together
    book3 = (book1 + book2) / 2

    # Total number of chapters Brian read
    total_chapters = book1 + book2 + book3
    result = total_chapters
    return result

print(solution())