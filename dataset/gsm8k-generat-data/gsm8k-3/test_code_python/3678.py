def solution():
    """Tom plants a tree that is 1 year old and 5 feet tall.  It gains 3 feet per year.  How old is it when it is 23 feet tall?"""
    # Define the initial height and growth rate of the tree
    INITIAL_HEIGHT = 5
    GROWTH_RATE = 3

    # Define the target height of the tree
    TARGET_HEIGHT = 23

    # Initialize the age of the tree
    age = 1

    # Calculate the age of the tree when it reaches the target height
    while INITIAL_HEIGHT < TARGET_HEIGHT:
        age += 1
        INITIAL_HEIGHT += GROWTH_RATE

    # Display the age of the tree when it reaches the target height
    result = age
    return result

print(solution())