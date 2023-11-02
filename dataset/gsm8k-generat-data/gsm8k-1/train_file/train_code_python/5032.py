def solution():
    """Ray always takes the same route when he walks his dog. First, he walks 4 blocks to the park. Then he walks 7 blocks to the high school. Finally, he walks 11 blocks to get back home.
    Ray walks his dog 3 times each day.
    How many blocks does Ray's dog walk each day?"""
    blocks_to_park = 4
    blocks_to_high_school = 7
    blocks_to_home = 11
    total_blocks_walked = (blocks_to_park + blocks_to_high_school + blocks_to_home) * 3
    result = total_blocks_walked
    return result

print(solution())