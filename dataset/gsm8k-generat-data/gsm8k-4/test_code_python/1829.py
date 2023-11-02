def solution():
    """Harry needs to buy 5 spellbooks that each cost 5 gold, three potion kits that each cost 20 silver, and one owl that costs 28 gold. There are 9 silver to a gold. How much will Harry pay total, in silvers?"""
    # Define the prices of the items in gold
    spellbook_price_gold = 5
    potion_kit_price_gold = 0.2
    owl_price_gold = 28

    # Define the conversion rate from gold to silver
    gold_to_silver = 9

    # Calculate the total cost in gold
    total_cost_gold = (spellbook_price_gold * 5) + (potion_kit_price_gold * 3) + owl_price_gold

    # Convert the total cost to silver
    total_cost_silver = total_cost_gold * gold_to_silver

    # Return the result
    result = total_cost_silver
    return result

print(solution())