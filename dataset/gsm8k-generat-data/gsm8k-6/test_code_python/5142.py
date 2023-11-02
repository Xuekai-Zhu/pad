def solution():
    # Calculate the cost of buying 8 separate pints of paint
    cost_8_pints = 8 * 8  # $8.00 per pint

    # Calculate the cost of buying a gallon of paint
    cost_gallon = 55.00

    # Calculate the amount saved by buying a gallon of paint instead of 8 separate pints
    amount_saved = cost_8_pints - cost_gallon
    result = amount_saved
    return result

print(solution())