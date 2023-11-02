def solution():
    """Kayla and Kylie picked 200 apples total. Kayla picked 1/4 of the apples that Kylie picked. How many apples did Kayla pick?"""
    # Define the total number of apples picked
    total_apples = 200

    # Calculate the fraction of apples that Kayla picked compared to Kylie
    kayla_fraction = 1/4

    # Set up the equation to solve for the number of apples Kylie picked
    # Let x be the number of apples Kylie picked
    # Then Kayla picked x/4 apples
    # And x + x/4 = 200
    x = 160

    # Calculate the number of apples Kayla picked
    kayla_apples = x * kayla_fraction

    result = kayla_apples
    return result

print(solution())