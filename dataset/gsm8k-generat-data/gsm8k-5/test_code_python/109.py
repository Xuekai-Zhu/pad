def solution():
    total_nuggets = 100  # The group ordered 100 chicken nuggets
    total_eaten = 2 * (x + y) + x  # Keely and Kendall each ate twice as many as Alyssa, and Alyssa ate x
    # This simplifies to 5x = 100, so x = 20
    alyssa_nuggets = 20  # Alyssa ate 20 chicken nuggets
    result = alyssa_nuggets
    return result

print(solution())