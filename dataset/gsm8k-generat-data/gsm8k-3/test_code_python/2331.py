def solution():
    """Henri has 8 hours to watch movies and read. He watches one movie that is 3.5 hours and one movie that is 1.5 hours. He then decides to read. If he can read 10 words a minute, how many words does he read before his free time is up?"""
    # Define the length of each movie
    movie1 = 3.5
    movie2 = 1.5

    # Calculate the total time Henri spends watching movies
    movie_time = movie1 + movie2

    # Define the amount of time Henri has left to read
    read_time = 8 - movie_time

    # Calculate the number of words Henri can read
    words_read = read_time * 60 * 10

    # Display the number of words read
    result = words_read
    return result

print(solution())