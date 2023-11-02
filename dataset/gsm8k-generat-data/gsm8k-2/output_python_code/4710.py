def solution():
    """Anna is reading a 31-chapter textbook, but she skips all the chapters that are divisible by 3.
    If it takes her 20 minutes to read each chapter, how many hours does she spend reading total?"""
    total_chapters = 31
    read_chapters = total_chapters - (total_chapters // 3)
    time_per_chapter = 20/60  # convert minutes to hours
    total_time = read_chapters * time_per_chapter
    result = total_time
    return result

print(solution())