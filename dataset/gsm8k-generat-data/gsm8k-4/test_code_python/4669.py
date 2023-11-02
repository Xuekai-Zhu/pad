def solution():
    """Tom plays an online trading card game. His deck has 19 rare cards, 11 uncommon, and 30 commons. The rare cards cost $1, the uncommon are $.50, and the commons are $.25 each. How much did his deck cost?"""
    # Define the prices of rare, uncommon, and common cards
    rare_price = 1
    uncommon_price = 0.5
    common_price = 0.25

    # Calculate the total cost of the rare cards
    rare_cost = rare_price * 19

    # Calculate the total cost of the uncommon cards
    uncommon_cost = uncommon_price * 11

    # Calculate the total cost of the common cards
    common_cost = common_price * 30

    # Calculate the total cost of the deck
    total_cost = rare_cost + uncommon_cost + common_cost

    # return the result
    result = total_cost
    return result

print(solution())