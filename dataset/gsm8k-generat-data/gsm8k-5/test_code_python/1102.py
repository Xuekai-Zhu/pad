def solution():
    tiles_on_monday = 38
    books_on_monday = 75
    tiles_on_tuesday = 2 * tiles_on_monday
    books_on_tuesday = 3 * books_on_monday

    # Calculate the total number of times Carla counted something on Tuesday
    total_count = tiles_on_tuesday + books_on_tuesday
    result = total_count
    return result

print(solution())