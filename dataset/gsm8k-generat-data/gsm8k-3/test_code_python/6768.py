def solution():
    """Kate's hair is half as long as Emily's hair. Emily’s hair is 6 inches longer than Logan's hair. If Logan hair is 20 inches, how many inches is Kate's hair?"""
    # Define the length of Logan's hair
    LOGAN_HAIR = 20

    # Calculate the length of Emily's hair
    emily_hair = LOGAN_HAIR + 6

    # Calculate the length of Kate's hair
    kate_hair = emily_hair / 2

    # Display the length of Kate's hair
    result = kate_hair
    return result

print(solution())