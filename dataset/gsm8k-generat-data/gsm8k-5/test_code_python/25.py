def solution():
    # Number of tennis balls hit out of the first 100
    hit_first_100 = int(2/5 * 100)

    # Number of tennis balls hit out of the next 75
    hit_next_75 = int(1/3 * 75)

    # Total number of tennis balls hit
    total_hit = hit_first_100 + hit_next_75

    # Number of tennis balls not hit
    not_hit = 175 - total_hit
    result = not_hit
    return result

print(solution())