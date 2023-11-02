def solution():
    total_books = 4 * 400  # Total number of books on the four shelves
    distance_per_book = 0.1  # Assuming each book covers 0.1 miles

    # Calculate the total distance Karen bikes to the library and back
    total_distance = total_books * distance_per_book * 2
    result = total_distance
    return result

print(solution())