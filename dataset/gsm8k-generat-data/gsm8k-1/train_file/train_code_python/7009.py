def solution():
    """For a New Year’s Eve appetizer, Alex is serving caviar with potato chips and creme fraiche. He buys 3 individual bags of potato chips for $1.00 each and dollops each chip with some creme fraiche that costs $5.00 and then the $73.00 caviar.  This appetizer will serve 3 people. How much will this appetizer cost per person?"""
    chip_cost = 3*1
    creme_fraiche_cost = 5
    caviar_cost = 73
    total_cost = chip_cost + creme_fraiche_cost + caviar_cost
    cost_per_person = total_cost / 3
    result = cost_per_person
    
    return result

print(solution())