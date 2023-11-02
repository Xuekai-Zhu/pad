def solution():
    total_books = 20  # Peter and Kristin are each reading 20 fantasy novels
    peter_speed = 1/18  # Peter can read one book in 18 hours, so he reads at a speed of 1/18 books per hour
    kristin_speed = peter_speed / 3  # Peter reads three times as fast as Kristin, so Kristin's speed is 1/3 of Peter's speed

    # Calculate how long it will take Peter to read all 20 books
    peter_time = total_books * peter_speed

    # Calculate how long it will take Kristin to read half of her books
    kristin_books = total_books / 2
    kristin_time = kristin_books * kristin_speed
    result = kristin_time
    return result

print(solution())