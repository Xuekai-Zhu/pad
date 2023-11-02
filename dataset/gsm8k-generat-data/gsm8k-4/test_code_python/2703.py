def solution():
    """There are 6 boxes of crayons that hold 8 orange crayons. There are 7 boxes of crayons that have 5 blue crayons. There is 1 box of 11 red crayons. How many crayons are there in total?"""
    
    # Calculate the total number of orange crayons
    orange_crayons = 6 * 8

    # Calculate the total number of blue crayons
    blue_crayons = 7 * 5

    # Calculate the total number of red crayons
    red_crayons = 11

    # Calculate the total number of crayons
    total_crayons = orange_crayons + blue_crayons + red_crayons

    result = total_crayons
    return result

print(solution())