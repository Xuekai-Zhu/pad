def solution():
    """Christine figures it would take a pint of paint to paint the front and back of 1 door in her house. She has 8 doors to paint. 
    At the paint store, she can either buy 8 separate pints of paint for $8.00 a pint or a gallon of paint (which is the same as 8 pints) for a flat $55.00 
    How much money will she save if she buys the gallon of paint instead of 8 pints?"""
    # Define the number of doors to be painted and the price per pint and per gallon
    NUM_DOORS = 8
    PRICE_PER_PINT = 8
    PRICE_PER_GALLON = 55

    # Calculate the total number of pints needed and the total cost to buy individual pints
    total_pints = NUM_DOORS * 2
    individual_pint_cost = total_pints * PRICE_PER_PINT

    # Calculate the cost to buy a gallon of paint
    gallon_cost = PRICE_PER_GALLON

    # Determine which option is cheaper and calculate the savings
    if individual_pint_cost < gallon_cost:
        savings = 0
    else:
        savings = individual_pint_cost - gallon_cost

    result = savings
    return result

print(solution())