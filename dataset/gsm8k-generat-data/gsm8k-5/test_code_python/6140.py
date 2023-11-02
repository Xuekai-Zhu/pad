def solution():
    nikki_movie = 30  # Nikki's favorite movie is 30 hours long
    michael_movie = nikki_movie / 3  # Nikki's movie is three times as long as Michael's movie
    joyce_movie = michael_movie + 2  # Joyce's movie is 2 hours longer than Michael's movie
    ryn_movie = nikki_movie * 4/5  # Ryn's movie is 4/5 times as long as Nikki's favorite movie

    # Calculate the total number of hours of their favorite movies together
    total_hours = nikki_movie + michael_movie + joyce_movie + ryn_movie
    result = total_hours
    return result

print(solution())