def solution():
    depth = 300  # Depth of the riverbed from the base of the hill
    ratio = 1 / 4  # The depth is a quarter of the vertical distance between the riverbed and the peak of the hill

    # Calculate the height of the hill using the given ratio
    height = (depth / ratio) - depth
    result = height
    return result

print(solution())