def solution():
    brother_time_per_book = 8
    john_speed_multiplier = 1.6  # 60% faster than brother
    num_books = 3

    # Calculate John's time per book based on brother's time per book and John's speed multiplier
    john_time_per_book = brother_time_per_book / john_speed_multiplier

    # Calculate total time it takes John to read all 3 books
    total_time = john_time_per_book * num_books
    result = total_time
    return result

print(solution())