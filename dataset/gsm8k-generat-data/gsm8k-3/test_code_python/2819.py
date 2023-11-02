def solution():
    """Brian likes to read books.  He read one book that had 20 chapters, two books that had 15 chapters each, and one book that had half the chapters of the three previous books put together. How many chapters of books did Brian read?"""
    # Calculate the total chapters in the first book
    book1_chapters = 20

    # Calculate the total chapters in the two books with 15 chapters each
    book2_chapters = 15 * 2

    # Calculate the total chapters in the three previous books
    total_previous_chapters = book1_chapters + book2_chapters

    # Calculate the total chapters in the last book
    book3_chapters = total_previous_chapters / 2

    # Calculate the total chapters of all the books
    total_chapters = book1_chapters + book2_chapters + book3_chapters

    # Display the total chapters
    result = total_chapters
    return result

print(solution())