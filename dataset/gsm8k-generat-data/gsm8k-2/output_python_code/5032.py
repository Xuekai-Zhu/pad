def solution():
    """Ray always takes the same route when he walks his dog. First, he walks 4 blocks to the park. Then he walks 7 blocks to the high school. Finally, he walks 11 blocks to get back home. Ray walks his dog 3 times each day. How many blocks does Ray's dog walk each day?"""
    park_blocks = 4
    high_school_blocks = 7
    home_blocks = 11
    total_blocks = park_blocks + high_school_blocks + home_blocks
    daily_walk_blocks = total_blocks * 3
    result = daily_walk_blocks
    return result

print(solution())