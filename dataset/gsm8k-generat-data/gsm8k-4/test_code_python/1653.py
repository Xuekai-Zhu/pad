def solution():
    """A book has 8 chapters. Beth has read 2 chapters in 3 hours. If she continues reading at that rate, in how many hours will she be able to finish reading the remaining chapters?"""
    # Calculate the number of remaining chapters
    remaining_chapters = 8 - 2

    # Calculate the time it takes to read one chapter
    time_per_chapter = 3 / 2

    # Calculate the total time it will take to read the remaining chapters
    total_time = remaining_chapters * time_per_chapter

    # return the result
    result = total_time
    return result

print(solution())