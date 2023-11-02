def solution():
    blueberries_per_pint = 200  # James needs 200 blueberries to make a pint of blueberry jam
    quarts_per_pie = 1/4  # James needs 1/4 quart of blueberry jam to make a blueberry pie
    pints_per_quart = 2  # There are 2 pints per quart
    pies = 6  # James wants to make 6 blueberry pies

    # Calculate the total number of blueberries James needs to pick
    total_blueberries = blueberries_per_pint * pints_per_quart * quarts_per_pie * pies
    result = total_blueberries
    return result

print(solution())