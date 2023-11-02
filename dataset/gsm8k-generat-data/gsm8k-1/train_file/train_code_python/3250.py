def solution():
    """To keep himself busy in class, Michael makes rubber-band balls. He makes two sizes, large and small. A small ball uses 50 rubber bands. A large ball requires 300 rubber bands. Michael brought a 5,000 pack to class and already made 22 small balls. How many large balls can he make with the remaining rubber bands?"""
    small_ball_rubber = 50
    large_ball_rubber = 300
    pack_size = 5000
    small_balls_made = 22
    total_rubber_used = small_balls_made * small_ball_rubber
    remaining_rubber = pack_size - total_rubber_used
    large_balls_made = remaining_rubber // large_ball_rubber
    result = large_balls_made
    return result

print(solution())