def solution():
    movie_cost = 2000
    dvd_cost = 6
    dvd_price = dvd_cost * 2.5
    num_movies_per_day = 500
    num_days_per_week = 5
    num_weeks = 20

    # Calculate the total cost of making all the DVDs
    total_dvd_cost = dvd_cost * num_movies_per_day * num_days_per_week * num_weeks

    # Calculate the total revenue from selling all the DVDs
    total_revenue = dvd_price * num_movies_per_day * num_days_per_week * num_weeks

    # Calculate the total profit
    total_profit = total_revenue - (movie_cost + total_dvd_cost)
    result = total_profit
    return result

print(solution())