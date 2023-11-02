def solution():
    """For a New Year’s Eve appetizer, Alex is serving caviar with potato chips and creme fraiche.  He buys 3 individual bags of potato chips for $1.00 each and dollops each chip with some creme fraiche that costs $5.00 and then the $73.00 caviar.  This appetizer will serve 3 people.  How much will this appetizer cost per person?"""
    # Define the cost of the potato chips
    chips_cost = 3 * 1

    # Define the cost of the creme fraiche and caviar
    caviar_cost = 5 + 73

    # Calculate the total cost of the appetizer
    total_cost = chips_cost + caviar_cost

    # Calculate the cost per person
    cost_per_person = total_cost / 3

    # return the result
    result = cost_per_person
    return result

print(solution())