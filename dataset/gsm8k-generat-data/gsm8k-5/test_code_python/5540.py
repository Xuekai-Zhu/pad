def solution():
    field_distance = 24  # the total distance of the field is 24 kilometers
    mary_distance = 3/8 * field_distance  # Mary ran 3/8 of a 24-kilometer field
    edna_distance = (2/3) * mary_distance  # Edna ran 2/3 of the distance of Mary
    lucy_distance = (5/6) * edna_distance  # Lucy ran 5/6 of the distance of Edna

    # Calculate how many more kilometers Lucy should run to cover the same distance as Mary
    remaining_distance = mary_distance - lucy_distance
    result = remaining_distance
    return result

print(solution())