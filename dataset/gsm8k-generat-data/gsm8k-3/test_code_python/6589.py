def solution():
    """Billy has 8 hours of free time on each day of the weekend. He wants to spend 75% of his time playing video games and the rest of his time reading. He can read 60 pages an hour and his books all contain 80 pages. How many books does he read?"""
    # Define the number of hours Billy has per day
    HOURS_PER_DAY = 8

    # Calculate the number of hours Billy wants to spend playing video games each day
    video_game_hours = HOURS_PER_DAY * 0.75

    # Calculate the number of hours Billy will spend reading each day
    reading_hours = HOURS_PER_DAY - video_game_hours

    # Calculate the number of pages Billy can read each day
    pages_per_hour = 60
    pages_per_book = 80
    pages_read = reading_hours * pages_per_hour

    # Calculate the number of books Billy can read
    books_read = pages_read / pages_per_book

    # Display the number of books Billy can read
    result = books_read
    return result

print(solution())