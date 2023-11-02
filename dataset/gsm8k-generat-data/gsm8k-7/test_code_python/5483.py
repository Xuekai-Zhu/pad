def solution():
    num_shelves = 4
    books_per_shelf = 400
    total_books = num_shelves * books_per_shelf

    # Assume Karen bikes the same distance to and from the library
    distance_per_trip = 2 * total_books   # 1 book = 1 mile
    total_distance = distance_per_trip
    return total_distance

print(solution())