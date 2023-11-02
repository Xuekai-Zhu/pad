def solution():
    """An orphaned kitten was only 4 inches when he was found. In the next two weeks, he doubled in length, and by 4 months old, he had double in length again. What is its current length?"""
    # Define the initial length of the kitten
    initial_length = 4

    # Double the length of the kitten after two weeks
    length_after_two_weeks = initial_length * 2

    # Double the length of the kitten again after four months
    current_length = length_after_two_weeks * 2

    # return the result
    result = current_length
    return result

print(solution())