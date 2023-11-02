def solution():
    first_movie = 90
    second_movie = first_movie + 30
    popcorn_time = 10
    fry_time = popcorn_time * 2
    total_time = first_movie + second_movie + popcorn_time + fry_time
    total_time_in_hours = total_time / 60
    result = total_time_in_hours
    return result

print(solution())