def solution():
    """James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much. He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?"""
    # Define the cost of creating the movie and the cost of each DVD
    movie_creation_cost = 2000
    dvd_production_cost = 6

    # Define the price at which each DVD is sold
    dvd_price = 2.5 * dvd_production_cost

    # Calculate the profit from selling one DVD
    dvd_profit = dvd_price - dvd_production_cost

    # Calculate the profit from selling one movie
    movie_profit = (500 * dvd_profit)

    # Calculate the profit from selling movies for 20 weeks
    total_profit = movie_profit * (5 * 20)

    # Subtract the cost of creating the movie from the total profit to get the net profit
    net_profit = total_profit - movie_creation_cost

    # Return the result
    result = net_profit
    return result

print(solution())