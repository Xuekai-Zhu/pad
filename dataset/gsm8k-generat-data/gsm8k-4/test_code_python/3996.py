def solution():
    """If Buzz bought a pizza with 78 slices at a restaurant and then decided to share it with the waiter in the ratio of 5:8, with Buzz's ratio being 5, what's twenty less the number of slices of pizza that the waiter ate?"""
    # Calculate the total number of slices of pizza
    total_slices = 78

    # Calculate the ratio of the waiter
    waiter_ratio = 8 / (5 + 8)

    # Calculate the number of slices eaten by the waiter
    waiter_slices = waiter_ratio * total_slices

    # Calculate the number of slices left for Buzz
    buzz_slices = total_slices - waiter_slices

    # Calculate the result
    result = 20 - waiter_slices
    return result

print(solution())