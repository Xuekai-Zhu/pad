def solution():
    # Calculate the total number of chapters in the first two books
    first_two_books = 2 * 15

    # Calculate the total number of chapters in the first three books
    first_three_books = 20 + first_two_books

    # Calculate the total number of chapters in the fourth book
    fourth_book = 0.5 * first_three_books

    # Calculate the total number of chapters read
    total_chapters = first_three_books + fourth_book
    result = total_chapters
    return result

print(solution())