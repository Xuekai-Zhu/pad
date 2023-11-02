def solution():
    # Calculate the total time Henri spends watching movies
    total_movie_time = 3.5 + 1.5  

    # Calculate the remaining time Henri has for reading
    remaining_time = 8 - total_movie_time  

    # Calculate how many words Henri can read in the remaining time
    words_read = remaining_time * 60 * 10  # Henri can read 10 words per minute

    result = words_read
    return result

print(solution())