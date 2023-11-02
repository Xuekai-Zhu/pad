def solution():
    
    first_movie = 2
    second_movie = first_movie * 1.5
    third_movie = (first_movie + second_movie) - 1
    marathon_length = first_movie + second_movie + third_movie
    result = marathon_length
    return result

print(solution())