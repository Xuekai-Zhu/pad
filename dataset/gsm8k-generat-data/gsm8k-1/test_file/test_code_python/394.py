def solution():
    """Nancy is cleaning out her old woodshed. She saw 90 spiders, 1/3rd as many millipedes as spiders, and a number of stink bugs equal to twice the number of millipedes minus 12. How many bugs did she count total?"""
    
    spiders = 90
    millipedes = spiders / 3
    stink_bugs = 2 * millipedes - 12
    total_bugs = spiders + millipedes + stink_bugs
    result = total_bugs
    return result

print(solution())