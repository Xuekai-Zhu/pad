def solution():
    free_time_per_day = 8
    weekend_days = 2
    total_free_time = free_time_per_day * weekend_days

    # Calculate the amount of time Billy wants to spend playing video games
    video_game_time = total_free_time * 0.75

    # Calculate the amount of time Billy will spend reading
    reading_time = total_free_time - video_game_time

    # Calculate how many pages Billy can read
    pages_can_read = reading_time * 60

    # Calculate how many books Billy can read
    books_can_read = pages_can_read / 80
    result = books_can_read
    return result

print(solution())