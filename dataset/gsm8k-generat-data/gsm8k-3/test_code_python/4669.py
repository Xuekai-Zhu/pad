def solution():
    """Tom plays an online trading card game. His deck has 19 rare cards, 11 uncommon, and 30 commons. The rare cards cost $1, the uncommon are $.50, and the commons are $.25 each. How much did his deck cost?"""
    # Define the cost of each type of card
    RARE_COST = 1
    UNCOMMON_COST = 0.5
    COMMON_COST = 0.25

    # Define the number of each type of card in Tom's deck
    rare_cards = 19
    uncommon_cards = 11
    common_cards = 30

    # Calculate the total cost of the rare cards
    rare_cost = rare_cards * RARE_COST

    # Calculate the total cost of the uncommon cards
    uncommon_cost = uncommon_cards * UNCOMMON_COST

    # Calculate the total cost of the common cards
    common_cost = common_cards * COMMON_COST

    # Calculate the total cost of the deck
    total_cost = rare_cost + uncommon_cost + common_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())