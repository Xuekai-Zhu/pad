def solution():
    """
    The town of Belize has 400 homes. One fourth of the town's homes are white. 
    One fifth of the non-white homes have a fireplace. How many of the non-white homes do not have a fireplace?
    """
    # Define the total number of homes and the number of white homes
    total_homes = 400
    white_homes = total_homes / 4

    # Define the number of non-white homes and the number of non-white homes with fireplace
    non_white_homes = total_homes - white_homes
    non_white_with_fireplace = non_white_homes / 5

    # Calculate the number of non-white homes without a fireplace
    non_white_without_fireplace = non_white_homes - non_white_with_fireplace

    result = non_white_without_fireplace
    return result

print(solution())