def solution():
    """A cat has nine lives. A dog has 3 less lives than a cat. A mouse has 7 more lives than a dog. How many lives does a mouse have?"""
    # Define the number of lives of a cat
    cat_lives = 9

    # Define the number of lives of a dog
    dog_lives = cat_lives - 3

    # Define the number of lives of a mouse
    mouse_lives = dog_lives + 7

    # Return the number of lives of a mouse
    result = mouse_lives
    return result

print(solution())