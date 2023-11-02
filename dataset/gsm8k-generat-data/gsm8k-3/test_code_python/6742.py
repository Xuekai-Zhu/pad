def solution():
    """An orphaned kitten was only 4 inches when he was found. In the next two weeks, he doubled in length, and by 4 months old, he had double in length again. What is its current length?"""
    # Define the kitten's initial length
    initial_length = 4

    # Calculate the kitten's length after two weeks
    length_after_2_weeks = initial_length * 2

    # Calculate the kitten's length after 4 months
    length_after_4_months = length_after_2_weeks * 2

    # Display the kitten's current length
    result = length_after_4_months
    return result

print(solution())