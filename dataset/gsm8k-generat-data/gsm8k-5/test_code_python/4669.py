def solution():
    rare_cards = 19
    uncommon_cards = 11
    common_cards = 30
    rare_card_cost = 1
    uncommon_card_cost = 0.5
    common_card_cost = 0.25

    # Calculate the cost of the rare cards
    rare_cards_cost = rare_cards * rare_card_cost

    # Calculate the cost of the uncommon cards
    uncommon_cards_cost = uncommon_cards * uncommon_card_cost

    # Calculate the cost of the common cards
    common_cards_cost = common_cards * common_card_cost

    # Calculate the total cost of the deck
    total_cost = rare_cards_cost + uncommon_cards_cost + common_cards_cost
    result = total_cost
    return result

print(solution())