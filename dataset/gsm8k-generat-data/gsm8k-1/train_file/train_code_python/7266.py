def solution():
    """James orders an 8 piece pizza. His friend eats 2 slices and James eats half of what is left. How many slices does James eat?"""
    pizza_slices = 8
    friend_slices = 2
    remaining_slices = pizza_slices - friend_slices
    james_slices = remaining_slices / 2
    result = james_slices
    return result

print(solution())