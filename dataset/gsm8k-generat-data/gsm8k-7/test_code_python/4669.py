def solution():
    num_rare_cards = 19
    rare_card_cost = 1

    num_uncommon_cards = 11
    uncommon_card_cost = 0.5

    num_common_cards = 30
    common_card_cost = 0.25

    # Calculate the total cost of all rare cards
    total_rare_cost = num_rare_cards * rare_card_cost

    # Calculate the total cost of all uncommon cards
    total_uncommon_cost = num_uncommon_cards * uncommon_card_cost

    # Calculate the total cost of all common cards
    total_common_cost = num_common_cards * common_card_cost

    # Calculate the total cost of the entire deck
    total_cost = total_rare_cost + total_uncommon_cost + total_common_cost
    result = total_cost
    return result

print(solution())