def solution():
    """The basketball team is practicing their free-throws, making as many as they can in one minute. DeShawn made 12 free-throws, and Kayla made 50% more than DeShawn. If Annieka made 4 fewer than Kayla, how many did Annieka make?"""
    # Calculate the number of free-throws Kayla made
    deshawn_free_throws = 12
    kayla_free_throws = deshawn_free_throws * 1.5

    # Calculate the number of free-throws Annieka made
    annieka_free_throws = kayla_free_throws - 4

    # Display the number of free-throws Annieka made
    result = annieka_free_throws
    return result

print(solution())