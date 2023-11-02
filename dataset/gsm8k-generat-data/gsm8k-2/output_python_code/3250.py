def solution():
    """To keep himself busy in class, Michael makes rubber-band balls. He makes two sizes, large and small. A small ball uses 50 rubber bands. A large ball requires 300 rubber bands. Michael brought a 5,000 pack to class and already made 22 small balls. How many large balls can he make with the remaining rubber bands?"""
    small_bands = 50
    large_bands = 300
    total_bands = 5000
    small_balls = 22
    used_bands = small_balls * small_bands
    remaining_bands = total_bands - used_bands
    large_balls = remaining_bands // large_bands
    result = large_balls
    return result

print(solution())