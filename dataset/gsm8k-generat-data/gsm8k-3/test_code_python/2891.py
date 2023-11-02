def solution():
    """The base of a hill located beside a river is 300m above the seabed. If this depth is a quarter of the vertical distance between the riverbed and the peak of the hill, how high is the hill?"""
    # Let x be the vertical distance between the riverbed and the peak of the hill
    # Then, according to the problem, we have:

    x / 4 = 300

    # Solving for x, we get:

    x = 4 * 300
    x = 1200

    # Therefore, the height of the hill is the vertical distance between the riverbed and the peak, which is x meters:

    result = x
    return result

print(solution())