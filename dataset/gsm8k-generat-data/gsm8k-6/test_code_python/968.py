def solution():
    # Calculate the number of shirts Mary gives away
    blue_shirts_given = 26 / 2
    brown_shirts_given = 36 / 3

    # Calculate the total number of shirts Mary has left
    total_blue_shirts = 26 - blue_shirts_given
    total_brown_shirts = 36 - brown_shirts_given
    total_shirts = total_blue_shirts + total_brown_shirts

    result = total_shirts
    return result

print(solution())