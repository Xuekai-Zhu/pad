def solution():
    """Anna is reading a 31-chapter textbook, but she skips all the chapters that are divisible by 3. If it takes her 20 minutes to read each chapter, how many hours does she spend reading total?"""
    total_chapters = 31
    skipped_chapters = total_chapters // 3
    chapters_read = total_chapters - skipped_chapters
    minutes_per_chapter = 20
    total_minutes = chapters_read * minutes_per_chapter
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())