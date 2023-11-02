def solution():
    """A milk teas shop was able to sell a total of 50 cups of milk tea yesterday. Two-fifths of their sales are winter melon flavor, three-tenths are Okinawa flavor, and the rest are chocolate flavor. How many cups of chocolate-flavored milk tea were they able to sell yesterday?"""
    # Calculate the number of cups sold for each flavor
    winter_melon_cups = 50 * 2/5
    okinawa_cups = 50 * 3/10
    chocolate_cups = 50 - winter_melon_cups - okinawa_cups

    # Display the number of cups of chocolate-flavored milk tea sold
    result = chocolate_cups
    return result

print(solution())