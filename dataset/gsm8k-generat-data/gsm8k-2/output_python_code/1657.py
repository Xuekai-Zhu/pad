def solution():
    """James needs 200 blueberries to make a pint of blueberry jam and then a quart of blueberry jam to make a blueberry pie. If there are two pints per quart, how many blueberries does James need to pick to make 6 pies?"""
    blueberries_per_pint = 200
    pints_per_quart = 2
    quarts_per_pie = 1/4
    pies = 6
    total_blueberries_needed = blueberries_per_pint * pints_per_quart * quarts_per_pie * pies
    result = total_blueberries_needed
    return result

print(solution())