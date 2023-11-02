def solution():
    """Christine figures it would take a pint of paint to paint the front and back of 1 door in her house. She has 8 doors to paint. At the paint store, she can either buy 8 separate pints of paint for $8.00 a pint or a gallon of paint (which is the same as 8 pints) for a flat $55.00 How much money will she save if she buys the gallon of paint instead of 8 pints?"""
    doors_to_paint = 8
    pints_per_door = 2
    pints_per_gallon = 8
    price_per_pint = 8
    price_per_gallon = 55

    total_pints_needed = doors_to_paint * pints_per_door
    pints_needed_per_gallon = pints_per_gallon

    pints_to_buy_separately = total_pints_needed
    pints_to_buy_in_gallon = (total_pints_needed // pints_needed_per_gallon + (total_pints_needed % pints_needed_per_gallon > 0)) * pints_needed_per_gallon

    cost_to_buy_separately = pints_to_buy_separately * price_per_pint
    cost_to_buy_gallon = price_per_gallon

    savings = cost_to_buy_separately - cost_to_buy_gallon
    result = savings
    return result

print(solution())