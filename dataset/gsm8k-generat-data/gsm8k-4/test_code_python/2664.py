def solution():
    """At a pool party, there are 4 pizzas cut into 12 slices each. If the guests eat 39 slices, how many slices are left?"""
    # Define the total number of pizza slices
    total_slices = 4 * 12

    # Subtract the number of slices eaten by the guests
    remaining_slices = total_slices - 39

    # return the result
    result = remaining_slices
    return result

print(solution())