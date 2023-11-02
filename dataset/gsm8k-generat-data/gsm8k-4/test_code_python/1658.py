def solution():
    """James needs 200 blueberries to make a pint of blueberry jam and then a quart of blueberry jam to make a blueberry pie. If there are two pints per quart, how many blueberries does James need to pick to make 6 pies?"""
    # Define the number of blueberries needed per pint of jam and per quart of pie filling
    blueberries_per_pint = 200
    blueberries_per_quart = blueberries_per_pint * 2

    # Calculate the number of blueberries needed to make 1 pie
    blueberries_per_pie = blueberries_per_quart * 4

    # Calculate the total number of blueberries needed to make 6 pies
    total_blueberries = blueberries_per_pie * 6

    # return the result
    result = total_blueberries
    return result

print(solution())