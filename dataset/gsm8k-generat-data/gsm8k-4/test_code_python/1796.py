def solution():
    """Dennis collected 10 rocks. He put all of them in his aquarium but his fish ate half of them. He was able to make the fish spit two out. How many of Dennis's rocks are left?"""
    # Define the initial number of rocks collected
    initial_rocks = 10

    # Calculate the number of rocks left after the fish ate half
    rocks_left = initial_rocks // 2

    # Add the two rocks that were spit out by the fish
    rocks_left += 2

    result = rocks_left
    return result

print(solution())