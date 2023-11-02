def solution():
    """Dennis collected 10 rocks. He put all of them in his aquarium but his fish ate half of them. He was able to make the fish spit two out. How many of Dennis's rocks are left?"""
    starting_rocks = 10
    eaten_rocks = starting_rocks / 2
    spit_out_rocks = 2
    remaining_rocks = starting_rocks - eaten_rocks + spit_out_rocks
    result = remaining_rocks
    return result

print(solution())