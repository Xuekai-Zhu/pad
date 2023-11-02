def solution():
    blueberries_per_pint = 200
    blueberries_per_quart = blueberries_per_pint * 2
    pies_to_make = 6

    # Calculate the total number of blueberries needed for all the pies
    total_blueberries_needed = blueberries_per_quart * pies_to_make

    result = total_blueberries_needed
    return result

print(solution())