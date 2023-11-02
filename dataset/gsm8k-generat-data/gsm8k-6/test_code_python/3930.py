def solution():
    # Calculate the amount of time Jonsey is awake and playing outside
    j_play_outside = (2/3) * (1/2)

    # Calculate the amount of time Jonsey is awake and inside
    j_inside = (2/3) - j_play_outside

    # Calculate the amount of time Riley is awake and playing outside
    r_play_outside = (3/4) * (1/3)

    # Calculate the amount of time Riley is awake and inside
    r_inside = (3/4) - r_play_outside

    # Calculate the average time they spend inside
    avg_inside = (j_inside + r_inside) / 2

    result = avg_inside
    return result

print(solution())