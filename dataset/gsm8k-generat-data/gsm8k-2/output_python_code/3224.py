def solution():
    """Chris bought 8 movies on DVD for $12 each and 4 movies on Blu-ray for $18 each. What is the average price he paid per movie?"""
    num_dvds = 8
    dvd_price = 12
    num_blurays = 4
    bluray_price = 18
    total_cost = (num_dvds * dvd_price) + (num_blurays * bluray_price)
    num_movies = num_dvds + num_blurays
    avg_price = total_cost / num_movies
    result = avg_price
    return result

print(solution())