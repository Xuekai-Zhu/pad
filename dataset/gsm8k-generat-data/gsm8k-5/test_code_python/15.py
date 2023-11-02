def solution():
    movie_cost = 2000  # James spends $2000 to create the movie
    dvd_cost = 6  # Each DVD costs $6 to make
    dvd_price = 2.5 * dvd_cost  # James sells each DVD for 2.5 times the cost to make it
    daily_sales = 500  # James sells 500 DVDs a day
    days_per_week = 5  # James works 5 days a week
    weeks = 20  # James wants to know his profit after 20 weeks

    # Calculate the total revenue from DVD sales
    total_revenue = dvd_price * daily_sales * days_per_week * weeks

    # Calculate the total cost of producing the DVDs
    total_cost = dvd_cost * daily_sales * days_per_week * weeks + movie_cost

    # Calculate the overall profit
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())