def solution():
    """Liza reads 20 pages in an hour, and Suzie reads 15 pages in an hour. How many more pages does Liza read than Suzie in 3 hours?"""
    liza_speed = 20
    suzie_speed = 15
    liza_pages_read = liza_speed * 3
    suzie_pages_read = suzie_speed * 3
    difference = liza_pages_read - suzie_pages_read
    result = difference
    return result

print(solution())