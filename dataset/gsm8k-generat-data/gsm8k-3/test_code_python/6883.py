def solution():
    """John decides to replace all his VHS with DVDs. He can trade in his VHS for $2 each and then buy the DVDs for $10 each. If he has 100 movies, how much does it cost to replace his movies?"""
    # Define the value of each VHS and the cost of each DVD
    VHS_VALUE = 2
    DVD_COST = 10

    # Define the number of movies
    num_movies = 100

    # Calculate the value of the VHS trades
    vhs_value = VHS_VALUE * num_movies

    # Calculate the cost of the DVDs
    dvd_cost = DVD_COST * num_movies

    # Calculate the total cost
    total_cost = dvd_cost - vhs_value

    # Display the total cost
    result = total_cost
    return result

print(solution())