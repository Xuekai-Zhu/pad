def solution():
    """For a New Year’s Eve appetizer, Alex is serving caviar with potato chips and creme fraiche.  He buys 3 individual bags of potato chips for $1.00 each and dollops each chip with some creme fraiche that costs $5.00 and then the $73.00 caviar.  This appetizer will serve 3 people.  How much will this appetizer cost per person?"""
    # Define the cost of the potato chips, creme fraiche, and caviar
    CHIP_COST = 1
    CREME_FRAICHE_COST = 5
    CAVIAR_COST = 73

    # Calculate the total cost of the appetizer
    total_cost = (3 * CHIP_COST) + (3 * CREME_FRAICHE_COST) + CAVIAR_COST

    # Calculate the cost per person
    cost_per_person = total_cost / 3

    # Display the cost per person
    result = cost_per_person
    return result

print(solution())