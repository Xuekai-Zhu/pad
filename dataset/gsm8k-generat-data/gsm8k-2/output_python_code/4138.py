def solution():
    """Eric has 4 ninja throwing stars. His friend Chad has twice as many. Then Jeff bought 2 ninja stars from Chad. Jeff now has 6 throwing stars. How many ninja throwing stars do they have altogether?"""
    eric = 4
    chad = 2 * eric
    chad -= 2 # Jeff bought 2 stars from Chad
    jeff = 6
    total_stars = eric + chad + jeff
    result = total_stars
    return result

print(solution())