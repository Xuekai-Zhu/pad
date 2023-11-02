def solution():
    """Chris bought 8 movies on DVD for $12 each and 4 movies on Blu-ray for $18 each. What is the average price he paid per movie?"""
    # Define the number of movies and their prices
    dvd_movies = 8
    dvd_price = 12
    bluray_movies = 4
    bluray_price = 18

    # Calculate the total amount spent on DVDs
    dvd_total = dvd_movies * dvd_price

    # Calculate the total amount spent on Blu-rays
    bluray_total = bluray_movies * bluray_price

    # Calculate the total number of movies
    total_movies = dvd_movies + bluray_movies

    # Calculate the average price per movie
    average_price = (dvd_total + bluray_total) / total_movies

    # return the result
    result = average_price
    return result

print(solution())