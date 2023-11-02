def solution():
    """Harry needs to buy 5 spellbooks that each cost 5 gold, three potion kits that each cost 20 silver, and one owl that costs 28 gold. There are 9 silver to a gold. How much will Harry pay total, in silvers?"""
    # Define the cost of each item in gold
    SPELLBOOK_PRICE = 5
    POTION_KIT_PRICE = 0.2  # 20 silver is 0.2 gold
    OWL_PRICE = 28

    # Define the exchange rate from gold to silver
    GOLD_TO_SILVER = 9

    # Calculate the total cost in gold
    total_cost_gold = 5 * SPELLBOOK_PRICE + 3 * POTION_KIT_PRICE + OWL_PRICE

    # Convert the total cost to silver
    total_cost_silver = total_cost_gold * GOLD_TO_SILVER

    # Display the total cost in silvers
    result = total_cost_silver
    return result

print(solution())