def solution():
    
    movie_length = 1.5
    num_replays = 6
    advertisement_time = 20 / 60
    total_operating_time = (movie_length + advertisement_time) * num_replays
    result = total_operating_time
    return result

print(solution())