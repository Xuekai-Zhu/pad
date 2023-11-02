def solution():
    """Pete's memory card can hold 3,000 pictures of 8 megabytes each. How many pictures can it hold of 6 megabytes each?"""
    max_pictures = 3000
    max_size = 8
    target_size = 6
    max_space = max_pictures * max_size
    target_space = max_space // (max_size // target_size)
    num_pictures = target_space // target_size
    result = num_pictures
    return result

print(solution())