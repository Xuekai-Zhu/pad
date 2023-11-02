def solution():
    
    total_chapters = 31
    skipped_chapters = total_chapters // 3
    chapters_read = total_chapters - skipped_chapters
    minutes_per_chapter = 20
    total_minutes = chapters_read * minutes_per_chapter
    total_hours = total_minutes / 60
    result = total_hours
    return result

print(solution())