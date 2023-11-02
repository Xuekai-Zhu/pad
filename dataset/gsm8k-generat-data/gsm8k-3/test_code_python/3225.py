def solution():
    """Chris bought 8 movies on DVD for $12 each and 4 movies on Blu-ray for $18 each. What is the average price he paid per movie?"""
    # Define the cost of each type of movie
    DVD_PRICE = 12
    BLU_RAY_PRICE = 18

    # Define the number of each type of movie purchased
    dvd_movies = 8
    blu_ray_movies = 4

    # Calculate the total cost of the DVD movies
    dvd_cost = dvd_movies * DVD_PRICE

    # Calculate the total cost of the Blu-ray movies
    blu_ray_cost = blu_ray_movies * BLU_RAY_PRICE

    # Calculate the total number of movies purchased
    total_movies = dvd_movies + blu_ray_movies

    # Calculate the average price per movie
    average_price = (dvd_cost + blu_ray_cost) / total_movies

    # Display the average price per movie
    result = average_price
    return result

print(solution())