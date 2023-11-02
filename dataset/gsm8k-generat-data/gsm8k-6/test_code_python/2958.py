def solution():
    # Calculate the number of white homes and non-white homes
    white_homes = 400 / 4  # one fourth of the town's homes are white
    non_white_homes = 400 - white_homes  # calculate the number of non-white homes 

    # Calculate the number of non-white homes with a fireplace
    homes_with_fireplace = (1/5) * (non_white_homes)  # one fifth of the non-white homes have a fireplace

    # Calculate the number of non-white homes without a fireplace
    homes_without_fireplace = non_white_homes - homes_with_fireplace

    result = homes_without_fireplace
    return result

print(solution())