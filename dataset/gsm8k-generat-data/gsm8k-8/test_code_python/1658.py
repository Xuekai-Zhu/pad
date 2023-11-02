def solution():
    # Calculate the number of blueberries needed for one quart of jam
    blueberries_per_quart = 200 * 2

    # Calculate the number of blueberries needed for one pie
    blueberries_per_pie = blueberries_per_quart * 4

    # Calculate the total number of blueberries needed for 6 pies
    total_blueberries = blueberries_per_pie * 6

    result = total_blueberries
    return result

print(solution())