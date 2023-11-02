def solution():
    """A milk teas shop was able to sell a total of 50 cups of milk tea yesterday. Two-fifths of their sales are winter melon flavor, three-tenths are Okinawa flavor, and the rest are chocolate flavor. How many cups of chocolate-flavored milk tea were they able to sell yesterday?"""
    total_cups_sold = 50
    winter_melon_cups = (2 / 5) * total_cups_sold
    okinawa_cups = (3 / 10) * total_cups_sold
    chocolate_cups = total_cups_sold - winter_melon_cups - okinawa_cups
    result = chocolate_cups
    return result

print(solution())