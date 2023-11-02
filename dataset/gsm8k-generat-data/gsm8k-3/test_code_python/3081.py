def solution():
    """A pea patch is twice as big as a radish patch. If one sixth of the pea patch is 5 square feet.  How much is a whole radish patch in square feet?"""
    # Define the size of one sixth of the pea patch
    PEA_PATCH_SIXTH = 5

    # Calculate the size of the whole pea patch
    pea_patch_size = PEA_PATCH_SIXTH * 6

    # Calculate the size of the radish patch
    radish_patch_size = pea_patch_size / 2

    # Display the size of the radish patch
    result = radish_patch_size
    return result

print(solution())