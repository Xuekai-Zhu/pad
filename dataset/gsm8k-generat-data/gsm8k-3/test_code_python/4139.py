def solution():
    """Eric has 4 ninja throwing stars. His friend Chad has twice as many. Then Jeff bought 2 ninja stars from Chad. Jeff now has 6 throwing stars. How many ninja throwing stars do they have altogether?"""
    # Define the number of throwing stars Eric has
    eric = 4

    # Calculate the number of throwing stars Chad has
    chad = eric * 2

    # Calculate the number of throwing stars Jeff bought from Chad
    jeff_bought = 2

    # Calculate the number of throwing stars Jeff has now
    jeff = 6

    # Calculate the total number of throwing stars
    total = eric + chad + jeff - jeff_bought

    # Display the total number of throwing stars
    result = total
    return result

print(solution())