def solution():
    # Calculate the number of chapters left to read
    chapters_left = 8 - 2

    # Calculate the time it takes to read one chapter
    time_per_chapter = 3 / 2

    # Calculate the total time it will take to finish reading the remaining chapters
    total_time = chapters_left * time_per_chapter
    result = total_time
    return result

print(solution())