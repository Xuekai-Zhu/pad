def solution():
    riverbed_to_hill = 4  # vertical distance between riverbed and peak is 4 times the depth
    depth = 300  # depth is 300m
    height = riverbed_to_hill * depth
    hill_height = height - depth  # subtract depth to get only the height of the hill itself
    result = hill_height
    return result

print(solution())