def solution():
    """John decides to take up an odd hobby of speed talking. His normally speaking speed is 150 WPM. After training his speed is 2.5 times faster than his starting speed. How long would it take him to speak 10 pages if each page has 450 words per page?"""
    normal_speed = 150
    trained_speed = normal_speed * 2.5
    words_per_page = 450
    pages = 10
    total_words = words_per_page * pages
    time_in_minutes = total_words / trained_speed
    result = time_in_minutes
    return result

print(solution())