def solution():
    # Define the number of eggs Megan bought
    eggs_bought = 2 * 12

    # Calculate the number of broken and cracked eggs
    eggs_broken = 3
    eggs_cracked = 2 * eggs_broken

    # Calculate the number of eggs that are still in perfect condition
    eggs_perfect = eggs_bought - eggs_broken - eggs_cracked

    # Calculate the difference between perfect eggs and cracked eggs
    difference = eggs_perfect - eggs_cracked
    result = difference
    return result

print(solution())