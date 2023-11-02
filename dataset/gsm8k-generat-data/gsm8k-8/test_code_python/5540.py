def solution():
    # Define Mary's distance and calculate Edna and Lucy's distances
    mary_distance = 3/8 * 24
    edna_distance = 2/3 * mary_distance
    lucy_distance = 5/6 * edna_distance

    # Calculate how many more kilometers Lucy needs to run to cover the same distance as Mary
    kilometers_to_cover = mary_distance - lucy_distance
    result = kilometers_to_cover
    return result

print(solution())