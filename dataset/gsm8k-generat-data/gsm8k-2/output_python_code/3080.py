def solution():
    """A pea patch is twice as big as a radish patch. If one sixth of the pea patch is 5 square feet. How much is a whole radish patch in square feet?"""
    pea_patch = 5 * 6 * 2  # one sixth of the pea patch is 5 square feet -> the whole pea patch is 6 * 5 = 30 square feet, and it's twice the size of the radish patch (so 2 * x = 30 -> x = 15)
    radish_patch = pea_patch / 2
    result = radish_patch
    return result

print(solution())