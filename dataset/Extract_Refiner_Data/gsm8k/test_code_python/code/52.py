def solution():
    
    # Define the prices of the movie tickets and popcorn
    ticket_price = 7
    popcorn_price = 7

    # Define the total amount of money Peter has
    total_money = 42

    # Calculate the maximum number of movies Peter can go to the movies
    max_movies = (total_money - ticket_price - popcorn_price) // movie_price

    # return the result
    result = max_movies
    return result

print(solution())