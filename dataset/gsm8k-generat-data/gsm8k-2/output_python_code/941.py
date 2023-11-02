def solution():
    """While Paul watches movies, he runs on his treadmill. He can run a mile in 12 minutes. He watches two movies, which are an average length of 1.5 hours. How many miles does he run?"""
    movie_length = 1.5 * 60 # Convert to minutes
    total_movie_length = 2 * movie_length
    miles_per_minute = 1 / 12 # Calculate how many miles per minute
    total_miles = miles_per_minute * total_movie_length
    result = total_miles
    return result

print(solution())