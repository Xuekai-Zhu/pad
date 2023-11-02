def solution():
    """Tim decides to do a movie marathon.  The first movie is 2 hours long.  The next movie is 50% longer.  And the last movie is 1 hour shorter than the combined time of the previous 2 movies.  How long was his movie marathon?"""
    # Calculate the length of the second movie
    second_movie = 2 * 1.5

    # Calculate the combined length of the first two movies
    first_two_movies = 2 + second_movie

    # Calculate the length of the third movie
    third_movie = first_two_movies - 1

    # Calculate the total length of the movie marathon
    total_length = first_two_movies + third_movie

    # Display the total length
    result = total_length
    return result

print(solution())