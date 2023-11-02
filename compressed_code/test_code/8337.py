def solution():
    
    dvd_price = 12
    blu_ray_price = 18
    dvd_count = 8
    blu_ray_count = 4
    total_cost = (dvd_price * dvd_count) + (blu_ray_price * blu_ray_count)
    total_movies = dvd_count + blu_ray_count
    average_price = total_cost / total_movies
    result = average_price
    return result

print(solution())