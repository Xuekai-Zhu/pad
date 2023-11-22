def solution():
    
    # Define the number of Fast and Furious movies
    num_fast_movies = 9
    num_furious_movies = 9

    # Define the total number of movies seen
    total_movies = num_fast_movies + num_furious_movies

    # Define the total amount spent
    total_spent = 216

    # Calculate the total number of tickets
    total_tickets = total_movies * 3

    # Calculate the average price per ticket
    avg_price = total_spent / total_tickets

    # Display the average price per ticket
    result = avg_price
    return result

print(solution())