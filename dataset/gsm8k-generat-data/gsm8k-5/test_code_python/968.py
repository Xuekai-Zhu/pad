def solution():
    blue_shirts = 26
    brown_shirts = 36

    # Calculate the number of blue shirts Mary will have after giving away half
    blue_shirts_given = blue_shirts / 2
    blue_shirts_remaining = blue_shirts - blue_shirts_given

    # Calculate the number of brown shirts Mary will have after giving away a third
    brown_shirts_given = brown_shirts / 3
    brown_shirts_remaining = brown_shirts - brown_shirts_given

    # Calculate the total number of shirts Mary will have remaining
    shirts_remaining = blue_shirts_remaining + brown_shirts_remaining

    result = shirts_remaining
    return result

print(solution())