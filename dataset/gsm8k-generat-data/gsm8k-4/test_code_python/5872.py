def solution():
    """If John travels 15 miles on a bike ride, and Jill travels 5 miles less, how many miles does Jim travel if he travels only 20% as far as Jill?"""
    # Define the distance traveled by John and Jill
    john_distance = 15
    jill_distance = john_distance - 5

    # Calculate the distance traveled by Jim
    jim_distance = jill_distance * 0.2

    # Return the result
    result = jim_distance
    return result

print(solution())