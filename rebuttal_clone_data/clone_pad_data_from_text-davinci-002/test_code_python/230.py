def solution():
    """Emery and Serena go to their school library, and each borrows a copy of The life of Jack Steve's book to read for their school project. If Emery can read five times as fast as Serena, and the book takes her 20 days to read, what's the average number of days the two take to read the book?"""
    Emery_read_rate = 5
    Serena_read_rate = 1
    total_read_rate = Emery_read_rate + Serena_read_rate
    Emery_read_time = 20
    Serena_read_time = Emery_read_time * (1 / Emery_read_rate)
    total_read_time = Emery_read_time + Serena_read_time
    average_read_time = total_read_time / total_read_rate
    result = average_read_time
    
    return result

print(solution())