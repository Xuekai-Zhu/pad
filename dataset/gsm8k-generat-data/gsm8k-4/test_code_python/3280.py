def solution():
    """Jonah decided to set up an aquarium. He started with 14 small fish. He added 2 more, but they ate 6 of his original fish before he could remove them and take them back to the store. He exchanged them for 3 new fish. How many fish does Jonah have now?"""
    # Define the initial number of fish
    fish = 14

    # Add 2 more fish
    fish += 2

    # Subtract the number of fish eaten
    fish -= 6

    # Add the number of new fish received
    fish += 3

    # return the result
    result = fish
    return result

print(solution())