def solution():
    # Let's call the number of Dodge trucks "x"
    # Then the number of Ford trucks would be 2 times the number of Toyota trucks, which we can call "y"
    # And the number of Toyota trucks would be twice the number of Volkswagen Bugs, which we know is 5, so there are 10 Toyota trucks
    # We also know that there are one-third as many Ford trucks as Dodge trucks, so y = x/3

    x = 15  # There are 15 Toyota trucks in the parking lot (2*5)
    y = x/3 * 2  # There are twice as many Ford trucks as Toyota trucks
    dodge_trucks = x + y + 5  # The total number of trucks in the parking lot is the sum of Dodge, Ford, Toyota, and Volkswagen
    result = dodge_trucks
    return result

print(solution())