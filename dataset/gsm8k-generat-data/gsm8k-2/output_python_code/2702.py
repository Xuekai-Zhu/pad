def solution():
    """There are 6 boxes of crayons that hold 8 orange crayons. There are 7 boxes of crayons that have 5 blue crayons. There is 1 box of 11 red crayons. How many crayons are there in total?"""
    total_orange = 6 * 8
    total_blue = 7 * 5
    total_red = 11
    total_crayons = total_orange + total_blue + total_red
    result = total_crayons
    return result

print(solution())