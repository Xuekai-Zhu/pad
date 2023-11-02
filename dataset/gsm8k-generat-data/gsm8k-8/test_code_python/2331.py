def solution():
    # Calculate the total time Henri spent watching movies
    movie_time = 3.5 + 1.5

    # Calculate the remaining time Henri has for reading
    reading_time = 8 - movie_time

    # Calculate the total number of minutes Henri has for reading
    total_reading_minutes = reading_time * 60

    # Calculate the total number of words Henri can read
    total_words = total_reading_minutes * 10

    result = total_words
    return result

print(solution())