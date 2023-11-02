def solution():
    """Bryce and four of his friends each ordered their own pizzas after football practice. Each pizza had 12 slices. Bryce and two friends ate 2/3 of their pizzas. The two remaining friends ate ¾ of their pizzas. How many slices of pizza were left?"""
    num_friends = 4
    num_slices = 12
    slices_eaten = ((1 + 2/3) * num_slices) + (2 * 3/4 * num_slices)
    slices_left = (num_friends + 1) * num_slices - slices_eaten
    result = slices_left
    return result

print(solution())