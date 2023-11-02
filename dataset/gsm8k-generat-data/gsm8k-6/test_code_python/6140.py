def solution():
    # Calculate the length of Michael's favorite movie
    michael_movie = (1/3) * 30  # Nikki's movie is three times as long as Michael's movie
    # Calculate the length of Joyce's favorite movie
    joyce_movie = michael_movie + 2  # Joyce's favorite movie is 2 hours longer than Michael's movie
    # Calculate the length of Ryn's favorite movie
    ryn_movie = (4/5) * 30  # Ryn's favorite movie is 4/5 times as long as Nikki's favorite movie
    # Calculate the total length of their favorite movies
    total = michael_movie + joyce_movie + nikki_movie + ryn_movie
    result = total
    return result

print(solution())