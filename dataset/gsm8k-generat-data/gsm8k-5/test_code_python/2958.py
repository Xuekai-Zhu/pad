def solution():
    total_homes = 400
    white_homes = total_homes / 4  # One fourth of the homes are white
    non_white_homes = total_homes - white_homes
    homes_with_fireplace = (non_white_homes / 5)  # One fifth of non-white homes have a fireplace
    homes_without_fireplace = non_white_homes - homes_with_fireplace
    result = homes_without_fireplace
    return result

print(solution())