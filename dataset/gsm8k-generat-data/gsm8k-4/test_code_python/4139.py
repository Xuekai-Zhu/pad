def solution():
    """Eric has 4 ninja throwing stars. His friend Chad has twice as many. Then Jeff bought 2 ninja stars from Chad. Jeff now has 6 throwing stars. How many ninja throwing stars do they have altogether?"""
    # Define Eric's initial number of throwing stars
    eric_stars = 4

    # Define Chad's number of throwing stars
    chad_stars = 2 * eric_stars

    # Subtract 2 stars from Chad and add them to Jeff's count
    jeff_stars = chad_stars - 2

    # Update Jeff's count to the given value
    jeff_stars = 6

    # Calculate the total number of throwing stars
    total_stars = eric_stars + chad_stars + jeff_stars

    # return the result
    result = total_stars
    return result

print(solution())