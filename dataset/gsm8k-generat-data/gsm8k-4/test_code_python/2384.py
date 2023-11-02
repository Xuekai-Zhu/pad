def solution():
    """Gerald wants to buy a meat pie that costs 2 pfennigs. Gerald has 54 farthings, and there are 6 farthings to a pfennig. How many pfennigs will Gerald have left after buying the pie?"""
    # Define the cost of the meat pie in farthings
    pie_cost = 2 * 6

    # Define the total amount of farthings Gerald has
    total_farthings = 54

    # Calculate the amount of farthings left after buying the pie
    farthings_left = total_farthings - pie_cost

    # Convert the remaining farthings to pfennigs
    pfennigs_left = farthings_left // 6

    # Return the result
    result = pfennigs_left
    return result

print(solution())