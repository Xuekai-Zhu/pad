def solution():
    """Kim has 12 nail polishes. Heidi has 5 more nail polishes than Kim, and Karen has 4 fewer nail polishes than Kim. How many nail polishes does Karen and Heidi have together?"""
    # Define the number of nail polishes Kim has
    kim_polishes = 12

    # Calculate the number of nail polishes Heidi has
    heidi_polishes = kim_polishes + 5

    # Calculate the number of nail polishes Karen has
    karen_polishes = kim_polishes - 4

    # Calculate the total number of nail polishes Heidi and Karen have together
    total = heidi_polishes + karen_polishes

    # Return the result
    result = total
    return result

print(solution())