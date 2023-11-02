def solution():
    # Calculate the total number of blueberries needed for 6 pies
    blueberries_per_pint = 200
    blueberries_per_quart = 2 * blueberries_per_pint
    blueberries_per_pie = blueberries_per_quart * 4  # 1 quart = 4 pints
    blueberries_for_6_pies = blueberries_per_pie * 6
    result = blueberries_for_6_pies
    return result

print(solution())