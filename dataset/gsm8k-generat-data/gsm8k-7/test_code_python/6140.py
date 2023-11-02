def solution():
    nikki_movie_length = 30

    # Calculate Michael's movie length
    michael_movie_length = nikki_movie_length / 3

    # Calculate Joyce's movie length
    joyce_movie_length = michael_movie_length + 2

    # Calculate Ryn's movie length
    ryn_movie_length = (4/5) * nikki_movie_length

    # Calculate the total length of their favorite movies
    total_movie_length = joyce_movie_length + michael_movie_length + nikki_movie_length + ryn_movie_length
    result = total_movie_length
    return result

print(solution())