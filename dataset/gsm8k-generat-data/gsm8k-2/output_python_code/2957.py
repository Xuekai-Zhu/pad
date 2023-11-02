def solution():
    """The town of Belize has 400 homes. One fourth of the town's homes are white. One fifth of the non-white homes have a fireplace. How many of the non-white homes do not have a fireplace?"""
    total_homes = 400
    white_homes = total_homes / 4
    non_white_homes = total_homes - white_homes
    fireplace_homes = (non_white_homes / 5)
    non_fireplace_homes = non_white_homes - fireplace_homes
    result = non_fireplace_homes
    return result

print(solution())