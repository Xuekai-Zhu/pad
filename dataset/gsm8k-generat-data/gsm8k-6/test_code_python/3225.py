def solution():
    # Calculate the total cost and the number of movies
    total_cost = 8 * 12 + 4 * 18  # 8 movies on DVD for $12 each and 4 movies on Blu-ray for $18 each
    num_movies = 8 + 4

    # Calculate the average price per movie
    average_price = total_cost / num_movies
    result = average_price
    return result

print(solution())