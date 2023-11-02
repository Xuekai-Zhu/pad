def solution():
    tiles_count = 38
    books_count = 75

    # Carla counts all the tiles twice
    tiles_count_on_tuesday = tiles_count * 2

    # Carla counts the books three times
    books_count_on_tuesday = books_count * 3

    # Calculate the total number of times Carla counted something on Tuesday
    total_count_on_tuesday = tiles_count_on_tuesday + books_count_on_tuesday
    result = total_count_on_tuesday
    return result

print(solution())