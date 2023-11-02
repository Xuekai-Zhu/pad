def solution():
    """A pea patch is twice as big as a radish patch. If one sixth of the pea patch is 5 square feet. How much is a whole radish patch in square feet?"""
    pea_patch = 5 * 6  # one sixth of the pea patch is 5, so the whole pea patch is 5 * 6 = 30 square feet
    radish_patch = pea_patch / 2  # the pea patch is twice as big as the radish patch
    result = radish_patch
    return result

print(solution())