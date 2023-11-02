def solution():
    # Calculate the total free time Billy has on the weekend
    total_time = 8 * 2  # 8 hours on Saturday + 8 hours on Sunday

    # Calculate the time he spends playing video games
    video_game_time = 0.75 * total_time

    # Calculate the time he spends reading
    reading_time = total_time - video_game_time

    # Calculate the number of books he can read
    pages_per_book = 80
    pages_per_hour = 60
    books = reading_time / (pages_per_hour * pages_per_book)

    result = books
    return result

print(solution())