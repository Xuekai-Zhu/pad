def solution():
    """The base of a hill located beside a river is 300m above the seabed. If this depth is a quarter of the vertical distance between the riverbed and the peak of the hill, how high is the hill?"""
    # Define the depth of the river and the height of the base of the hill
    river_depth = 300
    base_height = river_depth * 4

    # Calculate the total height of the hill
    hill_height = base_height + river_depth

    # return the result
    result = hill_height
    return result

print(solution())