def solution():
    """Mary has 5 green crayons and 8 blue crayons of different shades. If she gives out 3 green crayons and 1 blue crayon to Becky, how many crayons does she have left?"""
    green_crayons = 5
    blue_crayons = 8
    total_crayons = green_crayons + blue_crayons
    given_out_green = 3
    given_out_blue = 1
    crayons_left = total_crayons - (given_out_green + given_out_blue)
    result = crayons_left
    
    return result

print(solution())