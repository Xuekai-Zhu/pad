def solution():
    total_chapters = 31  # Anna is reading a 31-chapter textbook
    chapters_skipped = total_chapters // 3  # Anna skips all chapters that are divisible by 3
    chapters_read = total_chapters - chapters_skipped  # Anna only reads the remaining chapters
    time_per_chapter = 20  # It takes Anna 20 minutes to read each chapter

    # Calculate the total time Anna spends reading
    total_time = chapters_read * time_per_chapter
    # Convert the total time from minutes to hours
    total_time_hours = total_time / 60

    result = total_time_hours
    return result

print(solution())