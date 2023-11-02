def solution():
    """Pete's memory card can hold 3,000 pictures of 8 megabytes each. How many pictures can it hold of 6 megabytes each?"""
    original_size = 8
    new_size = 6
    original_capacity = 3000
    new_capacity = (original_size / new_size) * original_capacity
    result = new_capacity
    return result

print(solution())