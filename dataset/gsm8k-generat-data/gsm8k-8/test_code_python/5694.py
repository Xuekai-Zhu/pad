def solution():
    # Define the length of the first movie
    movie1_length = 2

    # Calculate the length of the second movie
    movie2_length = 1.5 * movie1_length

    # Calculate the combined length of the first two movies
    first_two_movies_length = movie1_length + movie2_length

    # Calculate the length of the third movie
    movie3_length = first_two_movies_length - 1

    # Calculate the total length of the movie marathon
    marathon_length = first_two_movies_length + movie3_length
    result = marathon_length
    return result

print(solution())