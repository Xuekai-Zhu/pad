def solution():
    
    movie_length = 1.5
    number_of_screenings = 6
    advertisement_time = 20 / 60
    total_screening_time = (movie_length + advertisement_time) * number_of_screenings
    result = total_screening_time
    return result

print(solution())