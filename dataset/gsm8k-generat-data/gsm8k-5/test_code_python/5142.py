def solution():
    doors_to_paint = 8  # Christine has 8 doors to paint
    pints_per_door = 2  # Christine needs a pint of paint for the front and back of each door
    pints_needed = doors_to_paint * pints_per_door  # Calculate the total number of pints needed

    # Calculate the cost of buying 8 pints separately
    cost_8_pints = pints_needed * 8.00

    # Calculate the cost of buying a gallon of paint
    cost_gallon = 55.00

    # Calculate the amount saved by buying a gallon of paint
    amount_saved = cost_8_pints - cost_gallon
    result = amount_saved
    return result

print(solution())