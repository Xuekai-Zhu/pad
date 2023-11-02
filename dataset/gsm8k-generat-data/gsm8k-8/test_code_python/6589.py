def solution():
    # Calculate the total free time Billy has on the weekend
    total_free_time = 8 * 2

    # Calculate the time Billy wants to spend playing video games
    video_game_time = total_free_time * 0.75

    # Calculate the time Billy has left for reading
    reading_time = total_free_time - video_game_time

    # Calculate the number of pages Billy can read
    total_pages_read = reading_time * 60

    # Calculate the number of books Billy can read
    num_books_read = total_pages_read // 80
    result = num_books_read
    return result

print(solution())