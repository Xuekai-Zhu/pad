def solution():
    """James creates a media empire. He creates a movie for $2000. Each DVD cost $6 to make. He sells it for 2.5 times that much. He sells 500 movies a day for 5 days a week. How much profit does he make in 20 weeks?"""
    # Define the cost and selling price of the movie
    movie_cost = 2000
    dvd_cost = 6
    dvd_price = 2.5 * dvd_cost

    # Calculate the profit per DVD
    profit_per_dvd = dvd_price - dvd_cost

    # Calculate the profit per day
    dvds_per_day = 500
    profit_per_day = dvds_per_day * profit_per_dvd

    # Calculate the profit per week
    days_per_week = 5
    profit_per_week = days_per_week * profit_per_day

    # Calculate the profit per 20 weeks
    weeks = 20
    total_profit = weeks * profit_per_week

    # Calculate the total cost of creating the movie
    total_cost = movie_cost + (dvd_cost * (dvds_per_day * days_per_week * weeks))

    # Calculate the net profit
    net_profit = total_profit - total_cost

    # Return the net profit
    result = net_profit
    return result

print(solution())