def solution():
    total_books = 20
    peter_speed = 3  # Peter is three times faster than Kristin

    peter_time_one_book = 18  # hours to read one book

    # Calculate Kristin's speed relative to Peter's speed
    kristin_speed = 1 / peter_speed

    # Calculate Kristin's time to read one book
    kristin_time_one_book = peter_time_one_book / kristin_speed

    # Calculate how long it will take Kristin to read half of her books
    half_books = total_books / 2
    time_half_books = kristin_time_one_book * half_books
    result = time_half_books
    return result

print(solution())