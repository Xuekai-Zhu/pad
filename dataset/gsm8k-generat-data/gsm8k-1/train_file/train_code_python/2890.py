def solution():
    """The base of a hill located beside a river is 300m above the seabed. If this depth is a quarter of the vertical distance between the riverbed and the peak of the hill, how high is the hill?"""
    seabed_to_base = 300
    seabed_to_peak = seabed_to_base / 0.25
    hill_height = seabed_to_peak - seabed_to_base
    result = hill_height
    return result

print(solution())