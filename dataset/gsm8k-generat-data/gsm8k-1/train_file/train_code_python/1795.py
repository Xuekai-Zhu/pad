def solution():
    """Dennis collected 10 rocks. He put all of them in his aquarium but his fish ate half of them. He was able to make the fish spit two out. How many of Dennis's rocks are left?"""
    initial_rocks = 10
    rocks_eaten = initial_rocks / 2
    rocks_spit_out = 2
    rocks_left = initial_rocks - rocks_eaten + rocks_spit_out
    result = rocks_left
    return result

print(solution())