def solution():
    free_time_per_day = 8  # Billy has 8 hours of free time on each day of the weekend
    video_game_time = free_time_per_day * 0.75  # Billy wants to spend 75% of his time playing video games
    reading_time = free_time_per_day - video_game_time  # Billy will spend the rest of his time reading

    # Calculate how many pages Billy can read during his reading time
    pages_read = reading_time * 60  # Billy can read 60 pages an hour
    pages_per_book = 80  # Billy's books all contain 80 pages

    # Calculate how many books Billy can read with the pages he has
    books_read = pages_read // pages_per_book  # Billy can only read whole books, not partial ones
    result = books_read
    return result

print(solution())