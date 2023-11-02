def solution():
    """Christine figures it would take a pint of paint to paint the front and back of 1 door in her house.  She has 8 doors to paint.  At the paint store, she can either buy 8 separate pints of paint for $8.00 a pint or a gallon of paint (which is the same as 8 pints) for a flat $55.00  How much money will she save if she buys the gallon of paint instead of 8 pints?"""
    # Define the cost of 1 pint and 1 gallon of paint
    PINT_PRICE = 8
    GALLON_PRICE = 55

    # Calculate the amount of paint needed
    paint_needed = 8 * 2 # 2 sides of each door

    # Calculate the cost of buying 8 separate pints of paint
    separate_pint_cost = PINT_PRICE * 8

    # Calculate the cost of buying 1 gallon of paint
    gallon_cost = GALLON_PRICE

    # Determine which option is cheaper
    if separate_pint_cost < gallon_cost:
        cheaper_option = "8 separate pints"
        savings = gallon_cost - separate_pint_cost
    else:
        cheaper_option = "1 gallon"
        savings = 0

    # Display the savings and the cheaper option
    result = (savings, cheaper_option)
    return result

print(solution())