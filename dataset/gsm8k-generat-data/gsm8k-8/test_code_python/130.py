def solution():
    # Define initial number of seashells
    num_seashells = 180

    # Give away seashells
    num_seashells -= 40
    num_seashells -= 30

    # Sell half of remaining seashells
    num_seashells /= 2

    result = num_seashells
    return result

print(solution())