def solution():
    """Toby is reading a book that is 45 pages long. It averages 200 words a page. Toby can read at a rate of 300 words per minute. He has to be at the airport in 60 minutes and plans to leave as soon as he finishes the book. It takes 10 minutes to get to the airport. How many minutes early will Toby be?"""
    num_pages = 45
    words_per_page = 200
    reading_rate = 300
    time_for_book = (num_pages * words_per_page) / reading_rate
    time_to_airport = 10
    total_time = time_for_book + time_to_airport
    early_time = 60 - total_time
    result = early_time
    return result

print(solution())