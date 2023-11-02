def solution():
    """A book has 8 chapters. Beth has read 2 chapters in 3 hours. If she continues reading at that rate, in how many hours will she be able to finish reading the remaining chapters?"""
    total_chapters = 8
    chapters_read = 2
    time_taken = 3
    chapters_remaining = total_chapters - chapters_read
    time_per_chapter = time_taken / chapters_read
    time_to_finish = time_per_chapter * chapters_remaining
    result = time_to_finish
    return result

print(solution())