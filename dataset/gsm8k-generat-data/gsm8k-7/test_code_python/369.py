def solution():
    mall_spending = 250
    movie_cost = 24
    num_movies = 3
    farmer_market_price = 1.25
    num_bags = 20

    # Calculate the total cost of the movies
    movie_cost_total = num_movies * movie_cost

    # Calculate the total cost of the beans
    bean_cost_total = num_bags * farmer_market_price

    # Calculate the total spending for the day
    total_spending = mall_spending + movie_cost_total + bean_cost_total
    result = total_spending
    return result

print(solution())