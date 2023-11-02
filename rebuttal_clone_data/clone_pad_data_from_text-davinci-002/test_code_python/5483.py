def solution():
    shelves = 4
    books_per_shelf = 400
    total_books = shelves * books_per_shelf
    miles_per_book = 1 / total_books
    round_trip = 2
    total_distance = round_trip * miles_per_book
    result = total_distance
    return result

print(solution())