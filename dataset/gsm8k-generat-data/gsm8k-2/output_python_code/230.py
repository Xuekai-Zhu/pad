def solution():
    """Emery and Serena go to their school library, and each borrows a copy of The life of Jack Steve's book to read for their school project.
    If Emery can read five times as fast as Serena, and the book takes her 20 days to read, what's the average number of days the two take to read the book?"""
    emery_time = 20
    serena_time = emery_time * 5
    total_time = emery_time + serena_time
    average_time = total_time / 2
    result = average_time
    return result

print(solution())