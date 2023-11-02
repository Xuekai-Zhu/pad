def solution():
    # Calculate the number of white homes
    white_homes = 400 // 4

    # Calculate the number of non-white homes
    non_white_homes = 400 - white_homes

    # Calculate the number of non-white homes with a fireplace
    homes_with_fireplace = (non_white_homes * (1 - 1/5))

    # Calculate the number of non-white homes without a fireplace
    homes_without_fireplace = non_white_homes - homes_with_fireplace

    result = homes_without_fireplace
    return result

print(solution())