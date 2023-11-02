def solution():
    """A small store made 50 posters to advertise their products. Two-fifths of them are small posters while half of them are medium posters. The rest are large posters. How many large posters are there?"""
    # Define the total number of posters
    total_posters = 50

    # Calculate the number of small posters
    small_posters = (2/5) * total_posters

    # Calculate the number of medium posters
    medium_posters = (1/2) * total_posters

    # Calculate the number of large posters
    large_posters = total_posters - small_posters - medium_posters

    # Display the number of large posters
    result = large_posters
    return result

print(solution())