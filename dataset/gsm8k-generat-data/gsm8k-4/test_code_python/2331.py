def solution():
    """Henri has 8 hours to watch movies and read. He watches one movie that is 3.5 hours and one movie that is 1.5 hours. He then decides to read. If he can read 10 words a minute, how many words does he read before his free time is up?"""
    # Define the total time Henri has
    total_time = 8

    # Define the time spent watching movies
    movie_time = 3.5 + 1.5

    # Define the time left for reading
    reading_time = total_time - movie_time

    # Calculate the total number of words Henri can read
    words_per_min = 10
    total_words = reading_time * 60 * words_per_min

    # Return the result
    result = total_words
    return result

print(solution())