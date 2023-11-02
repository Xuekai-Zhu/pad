def solution():
    """Kate's hair is half as long as Emily's hair. Emily’s hair is 6 inches longer than Logan's hair. If Logan hair is 20 inches, how many inches is Kate’s hair?"""
    # Define Logan's hair length
    logan_hair = 20

    # Calculate Emily's hair length
    emily_hair = logan_hair + 6

    # Calculate Kate's hair length
    kate_hair = emily_hair / 2

    # return the result
    result = kate_hair
    return result

print(solution())