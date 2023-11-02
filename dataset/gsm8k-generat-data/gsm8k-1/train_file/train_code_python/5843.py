def solution():
    """There are 3 consecutive odd integers that have a sum of -147. What is the largest number?"""
    sum_of_integers = -147
    # Let's call the smallest odd integer x
    # Then the next two consecutive integers are x + 2 and x + 4
    # Their sum is 3x + 6
    # We know that 3x + 6 = -147
    # Solving for x gives x = -51
    # So the three odd integers are -51, -49, and -47
    largest_integer = -47
    result = largest_integer
    return result

print(solution())