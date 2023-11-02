def solution():
    """A milk teas shop was able to sell a total of 50 cups of milk tea yesterday. Two-fifths of their sales are winter melon flavor, three-tenths are Okinawa flavor, and the rest are chocolate flavor. How many cups of chocolate-flavored milk tea were they able to sell yesterday?"""
    # Define the total number of cups sold
    total_cups = 50

    # Calculate the number of cups sold for winter melon and Okinawa flavors
    winter_melon_cups = total_cups * (2/5)
    okinawa_cups = total_cups * (3/10)

    # Calculate the number of cups sold for chocolate flavor
    chocolate_cups = total_cups - winter_melon_cups - okinawa_cups

    # return the result
    result = chocolate_cups
    return result

print(solution())