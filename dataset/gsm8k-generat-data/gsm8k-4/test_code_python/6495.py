def solution():
    """Every tree that Bart cuts down gives him 75 pieces of firewood. If he burns 5 logs a day from November 1 through February 28, how many trees will he need to cut down?"""
    # Define the number of days in the burning season
    burning_season_days = 120

    # Define the number of logs burned each day
    logs_burned_per_day = 5

    # Calculate the total number of logs burned in the burning season
    total_logs_burned = burning_season_days * logs_burned_per_day

    # Calculate the total number of firewood pieces needed
    firewood_pieces_needed = total_logs_burned * 1

    # Calculate the number of trees needed to produce the necessary firewood pieces
    trees_needed = firewood_pieces_needed / 75

    # Round up to the nearest whole tree
    trees_needed = math.ceil(trees_needed)

    # return the result
    result = trees_needed
    return result

print(solution())