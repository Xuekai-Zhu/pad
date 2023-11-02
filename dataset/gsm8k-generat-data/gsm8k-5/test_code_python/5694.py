def solution():
    # Length of first movie
    first_movie = 2

    # Length of second movie, which is 50% longer than the first
    second_movie = first_movie * 1.5

    # Length of third movie, which is 1 hour less than the sum of the first two movies
    third_movie = first_movie + second_movie - 1

    # Total length of movie marathon
    total_length = first_movie + second_movie + third_movie

    result = total_length
    return result

print(solution())