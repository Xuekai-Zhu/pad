def solution():
    """Joyce, Michael, Nikki, and Ryn have a favorite movie. Joyce's favorite movie is 2 hours longer than Michael's movie. Nikki's movie is three times as long as Michael's movie, and Ryn's favorite movie is 4/5 times as long as Nikki's favorite movie. If Nikki's favorite movie is 30 hours long, calculate the total number of hours of their favorite movies together."""
    # Define the length of Nikki's favorite movie
    nikki_movie = 30

    # Calculate the length of Michael's favorite movie
    michael_movie = nikki_movie / 3

    # Calculate the length of Joyce's favorite movie
    joyce_movie = michael_movie + 2

    # Calculate the length of Ryn's favorite movie
    ryn_movie = nikki_movie * 4 / 5

    # Calculate the total length of their favorite movies
    total_length = joyce_movie + michael_movie + nikki_movie + ryn_movie

    # Display the total length
    result = total_length
    return result

print(solution())