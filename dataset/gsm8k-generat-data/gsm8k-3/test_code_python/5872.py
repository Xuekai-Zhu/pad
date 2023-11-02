def solution():
    """If John travels 15 miles on a bike ride, and Jill travels 5 miles less, how many miles does Jim travel if he travels only 20% as far as Jill?"""
    # Define John and Jill's distances
    john_distance = 15
    jill_distance = john_distance - 5

    # Calculate Jim's distance
    jim_distance = jill_distance * 0.2

    # Display Jim's distance
    result = jim_distance
    return result

print(solution())