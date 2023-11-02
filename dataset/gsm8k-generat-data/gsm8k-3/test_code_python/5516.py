def solution():
    """A cat has nine lives.  A dog has 3 less lives than a cat.  A mouse has 7 more lives than a dog.  How many lives does a mouse have?"""
    # Define the number of lives for a cat
    cat_lives = 9

    # Calculate the number of lives for a dog
    dog_lives = cat_lives - 3

    # Calculate the number of lives for a mouse
    mouse_lives = dog_lives + 7

    # Display the number of lives for a mouse
    result = mouse_lives
    return result

print(solution())