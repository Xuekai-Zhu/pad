def solution():
    """James needs 200 blueberries to make a pint of blueberry jam and then a quart of blueberry jam to make a blueberry pie. If there are two pints per quart, how many blueberries does James need to pick to make 6 pies?"""
    blueberries_per_pint = 200
    blueberries_per_quart = blueberries_per_pint * 2
    pies = 6
    blueberries_needed = blueberries_per_quart * pies
    result = blueberries_needed
    return result

print(solution())