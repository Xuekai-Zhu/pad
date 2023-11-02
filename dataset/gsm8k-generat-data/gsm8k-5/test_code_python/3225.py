def solution():
    dvd_price = 12  # Price per DVD
    blu_ray_price = 18  # Price per Blu-ray
    dvd_count = 8  # Number of DVDs purchased
    blu_ray_count = 4  # Number of Blu-rays purchased

    # Total amount spent on DVDs and Blu-rays
    total_spent = (dvd_count * dvd_price) + (blu_ray_count * blu_ray_price)

    # Total number of movies purchased
    total_movies = dvd_count + blu_ray_count

    # Calculate the average price per movie
    avg_price = total_spent / total_movies
    result = avg_price
    return result

print(solution())