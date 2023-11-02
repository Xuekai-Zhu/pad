def solution():
    movie_len = 1.5 # hours
    num_replays = 6
    ad_len = 20 # minutes

    total_len = (movie_len + ad_len/60) * num_replays # convert ad_len to hours
    result = total_len
    return result

print(solution())