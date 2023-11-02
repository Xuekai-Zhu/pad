def solution():
    """Tim decides to do a movie marathon. The first movie is 2 hours long. The next movie is 50% longer. And the last movie is 1 hour shorter than the combined time of the previous 2 movies. How long was his movie marathon?"""
    first_movie = 2
    second_movie = first_movie * 1.5
    third_movie = (first_movie + second_movie) - 1
    marathon_length = first_movie + second_movie + third_movie
    result = marathon_length
    return result

print(solution())