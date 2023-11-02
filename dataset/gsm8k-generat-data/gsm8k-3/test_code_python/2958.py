def solution():
    """The town of Belize has 400 homes. One fourth of the town's homes are white. One fifth of the non-white homes have a fireplace. How many of the non-white homes do not have a fireplace?"""
    # Define the number of homes in Belize and the fraction of white homes
    TOTAL_HOMES = 400
    WHITE_FRACTION = 1/4

    # Calculate the number of white homes and non-white homes
    white_homes = TOTAL_HOMES * WHITE_FRACTION
    non_white_homes = TOTAL_HOMES - white_homes

    # Calculate the number of non-white homes with a fireplace
    non_white_with_fireplace = (4/5) * (non_white_homes)

    # Calculate the number of non-white homes without a fireplace
    non_white_without_fireplace = non_white_homes - non_white_with_fireplace

    # Display the number of non-white homes without a fireplace
    result = non_white_without_fireplace
    return result

print(solution())