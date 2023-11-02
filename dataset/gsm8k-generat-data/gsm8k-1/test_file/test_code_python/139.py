def solution():
    """John buys milk for 2 dollars, eggs for 3 dollars, light bulbs for 3 dollars, cups for 3 dollars, and roach traps for 4 dollars. If there is a 10% tax on all nonfood items how much did everything cost."""
    milk_cost = 2
    eggs_cost = 3
    bulbs_cost = 3
    cups_cost = 3
    roach_traps_cost = 4
    non_food_items_cost = milk_cost + eggs_cost + bulbs_cost + cups_cost + roach_traps_cost
    non_food_items_tax = non_food_items_cost * 0.1
    total_cost = non_food_items_cost + non_food_items_tax
    result = total_cost
    return result

print(solution())