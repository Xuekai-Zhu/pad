def solution():
    """John decides to replace all his VHS with DVDs. He can trade in his VHS for $2 each and then buy the DVDs for $10 each. If he has 100 movies, how much does it cost to replace his movies?"""
    # Define the price of trading in each VHS and buying each DVD
    VHS_PRICE = 2
    DVD_PRICE = 10

    # Define the number of movies John has
    num_movies = 100

    # Calculate the total cost of replacing all his VHS with DVDs
    trade_in_cost = VHS_PRICE * num_movies
    dvd_cost = DVD_PRICE * num_movies
    total_cost = dvd_cost - trade_in_cost

    # return the result
    result = total_cost
    return result

print(solution())