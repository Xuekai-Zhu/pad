def solution():
    """Trey is raising money for a new bike that costs $112. He plans to spend the next two weeks selling bracelets for $1 each. On average, how many bracelets does he need to sell each day?"""
    # Define the cost of the bike and the number of days in two weeks
    BIKE_COST = 112
    DAYS_IN_TWO_WEEKS = 14

    # Calculate the total number of bracelets Trey needs to sell
    total_bracelets = BIKE_COST

    # Calculate the number of bracelets Trey needs to sell per day
    bracelets_per_day = total_bracelets / (DAYS_IN_TWO_WEEKS * 2)

    # Display the number of bracelets Trey needs to sell per day
    result = bracelets_per_day
    return result

print(solution())