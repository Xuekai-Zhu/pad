def solution():
    """Billy has 8 hours of free time on each day of the weekend. He wants to spend 75% of his time playing video games and the rest of his time reading. He can read 60 pages an hour and his books all contain 80 pages. How many books does he read?"""
    hours_per_day = 8
    percentage_for_video_games = 75
    percentage_for_reading = 100 - percentage_for_video_games
    hours_for_reading_per_day = (percentage_for_reading / 100) * hours_per_day
    pages_per_hour = 60
    pages_per_book = 80
    books_per_hour = pages_per_hour / pages_per_book
    total_books = hours_for_reading_per_day * books_per_hour * 2
    result = total_books
    return result

print(solution())