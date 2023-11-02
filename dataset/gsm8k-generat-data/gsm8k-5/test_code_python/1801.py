def solution():
    eggs_bought = 6 * 12  # Addilynn bought 6 dozen eggs, or 6*12=72 eggs
    eggs_used = eggs_bought / 2  # After two weeks, Addilynn used half of the eggs
    eggs_left = eggs_bought - eggs_used - 15  # Subtract the used and broken eggs from the total

    result = eggs_left
    return result

print(solution())