def solution():
    """Kylie and Kayla pick apples together and take home 340 apples total. If Kayla picked 10 more than 4 times the amount of apples that Kylie picked, how many apples did Kayla pick?"""
    # Let x be the number of apples Kylie picked
    # Then Kayla picked 4x + 10 apples
    # And the total number of apples is x + (4x + 10) = 5x + 10

    # Set up equation for total number of apples
    total = 340

    # Solve for x
    x = (total - 10) / 5

    # Calculate the number of apples Kayla picked (4x + 10)
    kayla = 4 * x + 10

    # Display the number of apples Kayla picked
    result = kayla
    return result

print(solution())