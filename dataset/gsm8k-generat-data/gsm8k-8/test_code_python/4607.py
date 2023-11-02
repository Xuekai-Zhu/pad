def solution():
    # Calculate Jim's original reading time in hours
    original_reading_time = 600 / 40

    # Calculate Jim's new reading time in hours
    new_reading_time = (original_reading_time - 4) * (2.5/2)

    # Calculate Jim's new reading speed in pages per hour
    new_reading_speed = 40 * 1.5

    # Calculate how many pages Jim reads per week now
    new_pages_read = new_reading_speed * new_reading_time

    result = new_pages_read
    return result

print(solution())