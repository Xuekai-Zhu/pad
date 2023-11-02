def solution():
    """Mike decides he wants to replace his movie collection with digital versions. He has 600 movies. A third of the movies are in various series and he knows he can get those for only $6 of the cost of a normal movie by just buying the series together. 40% of the remaining movies are older movies which are $5. How much does replacing the movies cost if a normal movie costs $10?"""
    total_movies = 600
    series_movies = total_movies / 3
    non_series_movies = total_movies - series_movies
    series_price = 6
    normal_price = 10
    older_movies = non_series_movies * 0.4
    older_movie_price = 5
    total_cost = (series_movies * series_price) + (non_series_movies - older_movies) * normal_price + older_movies * older_movie_price
    result = total_cost
    return result

print(solution())