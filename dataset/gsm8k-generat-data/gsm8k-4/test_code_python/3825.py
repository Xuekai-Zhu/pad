def solution():
    """There were 37 jellybeans in a jar. Pat removed 15 of them. Pat then added 5 of the removed jellybeans back in, and then removed 4 more. How many jellybeans are now in the jar?"""
    # Define the initial number of jellybeans
    initial_jellybeans = 37

    # Remove 15 jellybeans
    jellybeans_after_removal = initial_jellybeans - 15

    # Add 5 jellybeans back in
    jellybeans_after_addition = jellybeans_after_removal + 5

    # Remove 4 jellybeans
    jellybeans_now = jellybeans_after_addition - 4

    # return the result
    result = jellybeans_now
    return result

print(solution())