def solution():
    """A cat has nine lives. A dog has 3 less lives than a cat. A mouse has 7 more lives than a dog. How many lives does a mouse have?"""
    cat_lives = 9
    dog_lives = cat_lives - 3
    mouse_lives = dog_lives + 7
    result = mouse_lives
    return result

print(solution())