def solution():
    """A small store made 50 posters to advertise their products. 
    Two-fifths of them are small posters while half of them are medium posters. 
    The rest are large posters. How many large posters are there?"""
    total_posters = 50
    small_posters = (2/5) * total_posters
    medium_posters = 0.5 * total_posters
    large_posters = total_posters - small_posters - medium_posters
    result = large_posters
    return result

print(solution())