def solution():
    """Joyce, Michael, Nikki, and Ryn have a favorite movie. Joyce's favorite movie is 2 hours longer than Michael's movie. Nikki's movie is three times as long as Michael's movie, and Ryn's favorite movie is 4/5 times as long as Nikki's favorite movie. If Nikki's favorite movie is 30 hours long, calculate the total number of hours of their favorite movies together."""
    nikki_movie = 30
    michael_movie = nikki_movie / 3
    joyce_movie = michael_movie + 2
    ryn_movie = (4 / 5) * nikki_movie
    total_hours = nikki_movie + michael_movie + joyce_movie + ryn_movie
    result = total_hours
    return result

print(solution())