def solution():
    """Samuel is going to the cinema with his brother, Kevin. They both have a total budget of $20 for their outing. Samuel buys his $14 ticket, then spends $6 on drinks and food. Kevin buys his ticket, then spends $2 on drinks. They have both used their entire budget. How much did Kevin spend on food?"""
    # Define the cost of Samuel's ticket and his spending on drinks and food
    SAMUEL_TICKET = 14
    SAMUEL_SPENDING = 6

    # Define the cost of Kevin's ticket and his spending on drinks
    KEVIN_TICKET = 20 - SAMUEL_TICKET - SAMUEL_SPENDING
    KEVIN_DRINKS = 2

    # Calculate Kevin's spending on food
    KEVIN_FOOD = 20 - SAMUEL_TICKET - SAMUEL_SPENDING - KEVIN_TICKET - KEVIN_DRINKS

    # Display Kevin's spending on food
    result = KEVIN_FOOD
    return result

print(solution())