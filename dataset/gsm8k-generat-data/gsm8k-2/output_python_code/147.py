def solution():
    """Mary has 5 green crayons and 8 blue crayons of different shades. If she gives out 3 green crayons and 1 blue crayon to Becky, how many crayons does she have left?"""
    green_crayons = 5
    blue_crayons = 8
    green_crayons -= 3
    blue_crayons -= 1
    total_crayons = green_crayons + blue_crayons
    result = total_crayons
    return result

print(solution())