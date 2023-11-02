def solution():
    """Gerald wants to buy a meat pie that costs 2 pfennigs. Gerald has 54 farthings, and there are 6 farthings to a pfennig. How many pfennigs will Gerald have left after buying the pie?"""
    # Define the cost of the meat pie in pfennigs
    PIE_PRICE = 2

    # Define the conversion rate between farthings and pfennigs
    CONVERSION_RATE = 1 / 6

    # Convert Gerald's money to pfennigs
    total_money_pfennigs = 54 * CONVERSION_RATE

    # Calculate how many pfennigs Gerald will have left after buying the pie
    pfennigs_left = total_money_pfennigs - PIE_PRICE

    # Display how many pfennigs Gerald will have left
    result = pfennigs_left
    return result

print(solution())