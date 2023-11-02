def solution():
    mabel_distance = 4500  # Mabel lives 4500 steps directly east of Lake High School
    helen_distance = (3/4) * mabel_distance  # Helen lives 3/4 of the distance that Mabel lives

    # The total distance Mabel will walk to visit Helen is the sum of the distance between Mabel's house and the school,
    # the distance between Helen's house and the school, and the distance between Mabel's house and Helen's house
    total_distance = 2 * mabel_distance + 2 * helen_distance

    result = total_distance
    return result

print(solution())