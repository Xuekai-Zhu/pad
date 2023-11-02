def solution():
    # Find the ratio of books to total stationery
    book_ratio = 7 / (7+3)  # books : (books+pens)
    # Calculate the number of books Arlo bought
    total_stationery = 400
    books = int(book_ratio * total_stationery)
    result = books
    return result

print(solution())