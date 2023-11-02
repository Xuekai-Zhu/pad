def solution():
    """The bowl of fruit contains apples, pears, and bananas. There are two more pears than apples, and three more bananas than pears. If the bowl contains 19 pieces of fruit, how many bananas does it contain?"""
    # Initialize the number of apples
    apples = 0

    # Calculate the number of pears (which is two more than apples)
    pears = apples + 2

    # Calculate the number of bananas (which is three more than pears)
    bananas = pears + 3

    # Calculate the total number of fruits
    total_fruits = apples + pears + bananas

    # Check if the total number of fruits is equal to 19
    while total_fruits != 19:
        # Update the number of apples and pears
        apples += 1
        pears = apples + 2

        # Update the number of bananas
        bananas = pears + 3

        # Update the total number of fruits
        total_fruits = apples + pears + bananas

    # Return the number of bananas
    result = bananas
    return result

print(solution())