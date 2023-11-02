def solution():
    # Calculate the length of Nikki's movie
    nikki_movie = 30

    # Calculate the length of Michael's movie
    michael_movie = nikki_movie / 3

    # Calculate the length of Joyce's movie
    joyce_movie = michael_movie + 2

    # Calculate the length of Ryn's movie
    ryn_movie = 4/5 * nikki_movie

    # Calculate the total length of their favorite movies
    total_length = nikki_movie + michael_movie + joyce_movie + ryn_movie
    result = total_length
    return result

print(solution())