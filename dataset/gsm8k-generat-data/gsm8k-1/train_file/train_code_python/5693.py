def solution():
    """Tim decides to do a movie marathon. The first movie is 2 hours long. The next movie is 50% longer. And the last movie is 1 hour shorter than the combined time of the previous 2 movies. How long was his movie marathon?"""
    first_movie_length = 2
    second_movie_length = first_movie_length * 1.5
    total_previous_movie_length = first_movie_length + second_movie_length
    third_movie_length = total_previous_movie_length - 1
    movie_marathon_length = first_movie_length + second_movie_length + third_movie_length
    result = movie_marathon_length
    return result

print(solution())