def solution():
    # Calculate the distance each athlete ran
    mary_distance = (3/8) * 24
    edna_distance = (2/3) * mary_distance
    lucy_distance = (5/6) * edna_distance

    # Calculate how many more kilometers Lucy should run to cover the same distance as Mary
    additional_distance = mary_distance - lucy_distance
    result = additional_distance
    return result

print(solution())