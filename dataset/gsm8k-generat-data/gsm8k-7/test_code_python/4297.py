def solution():
    num_box1_movies = 10
    box1_movie_price = 2.0

    num_box2_movies = 5
    box2_movie_price = 5.0

    # Calculate the total cost of all movies in the first box
    total_box1_cost = num_box1_movies * box1_movie_price

    # Calculate the total cost of all movies in the second box
    total_box2_cost = num_box2_movies * box2_movie_price

    # Calculate the total number of movies that Duke bought
    total_num_movies = num_box1_movies + num_box2_movies

    # Calculate the total cost of all movies that Duke bought
    total_cost = total_box1_cost + total_box2_cost

    # Calculate the average price of each DVD
    average_price = total_cost / total_num_movies
    result = average_price
    return result

print(solution())