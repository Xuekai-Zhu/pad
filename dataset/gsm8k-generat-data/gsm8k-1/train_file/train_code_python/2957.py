def solution():
    """The town of Belize has 400 homes. One fourth of the town's homes are white. One fifth of the non-white homes have a fireplace. How many of the non-white homes do not have a fireplace?"""
    total_homes = 400
    white_homes = total_homes / 4
    non_white_homes = total_homes - white_homes
    non_white_with_fireplace = non_white_homes / 5
    non_white_without_fireplace = non_white_homes - non_white_with_fireplace
    result = non_white_without_fireplace
    return result

print(solution())