def solution():
    # Calculate the number of pages Jim reads per hour
    pages_per_hour = 40

    # Calculate Jim's initial number of reading hours per week
    initial_reading_hours = 600 / pages_per_hour

    # Calculate Jim's new reading speed and hours
    new_speed = 1.5 * pages_per_hour
    new_reading_hours = initial_reading_hours - 4

    # Calculate the new number of pages Jim reads per week
    new_reading_pages = new_speed * new_reading_hours

    result = new_reading_pages
    return result

print(solution())