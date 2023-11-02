def solution():
    """Billy has 8 hours of free time on each day of the weekend. He wants to spend 75% of his time playing video games and the rest of his time reading. He can read 60 pages an hour and his books all contain 80 pages. How many books does he read?"""
    total_weekend_hours = 16
    video_game_hours = total_weekend_hours * 0.75
    reading_hours = total_weekend_hours - video_game_hours
    pages_per_hour = 60
    pages_per_book = 80
    total_reading_pages = reading_hours * pages_per_hour * 2
    books_read = total_reading_pages // pages_per_book
    result = books_read
    return result

print(solution())