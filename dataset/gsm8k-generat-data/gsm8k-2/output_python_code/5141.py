def solution():
    """Christine figures it would take a pint of paint to paint the front and back of 1 door in her house. She has 8 doors to paint. At the paint store, she can either buy 8 separate pints of paint for $8.00 a pint or a gallon of paint (which is the same as 8 pints) for a flat $55.00 How much money will she save if she buys the gallon of paint instead of 8 pints?"""
    doors_to_paint = 8
    pint_price = 8.0
    gallon_price = 55.0
    pints_needed = doors_to_paint * 2
    num_gallons = pints_needed / 8
    price_per_door_with_pint = pint_price * 2
    price_per_door_with_gallon = (gallon_price / 8) * 2
    total_price_with_pint = price_per_door_with_pint * doors_to_paint
    total_price_with_gallon = price_per_door_with_gallon * doors_to_paint
    money_saved = total_price_with_pint - total_price_with_gallon
    result = money_saved
    return result

print(solution())