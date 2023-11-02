def solution():
    total_books = 3000
    lidia_books = total_books / 5  # Lidia's collection is 4 times bigger than Susan's, so Lidia has 4/5 of the total books
    susan_books = total_books - lidia_books  # Susan's collection is the remaining 1/5 of the total books
    result = susan_books
    return result

print(solution())