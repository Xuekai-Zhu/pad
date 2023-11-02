def solution():
    """A movie that's 1.5 hours long is being replayed 6 times in one movie theater each day. There is a 20-minute advertisement before the start of the movie. How long, in hours, does the movie theater operate each day?"""
    movie_length = 1.5
    number_of_screenings = 6
    advertisement_time = 20 / 60
    total_screening_time = (movie_length + advertisement_time) * number_of_screenings
    result = total_screening_time
    return result

print(solution())