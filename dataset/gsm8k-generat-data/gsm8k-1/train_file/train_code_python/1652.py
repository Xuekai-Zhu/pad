def solution():
    """A book has 8 chapters. Beth has read 2 chapters in 3 hours. If she continues reading at that rate, in how many hours will she be able to finish reading the remaining chapters?"""
    total_chapters = 8
    chapters_read = 2
    remaining_chapters = total_chapters - chapters_read
    time_per_chapter = 3
    total_time = remaining_chapters * time_per_chapter
    result = total_time
    return result

print(solution())