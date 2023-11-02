def solution():
    """
    Eric has 4 ninja throwing stars. His friend Chad has twice as many. Then Jeff bought 2 ninja stars from Chad. 
    Jeff now has 6 throwing stars. How many ninja throwing stars do they have altogether?
    """
    eric_stars = 4
    chad_stars = eric_stars * 2
    chad_stars -= 2   # Jeff bought 2 stars from Chad, so subtract those from Chad's total
    total_stars = eric_stars + chad_stars + 6   # Jeff now has 6 stars
    result = total_stars
    return result

print(solution())