def solution():
    """A milk teas shop was able to sell a total of 50 cups of milk tea yesterday. Two-fifths of their sales are winter melon flavor, three-tenths are Okinawa flavor, and the rest are chocolate flavor. How many cups of chocolate-flavored milk tea were they able to sell yesterday?"""
    total_sales = 50
    winter_melon_sales = 2/5 * total_sales
    okinawa_sales = 3/10 * total_sales
    chocolate_sales = total_sales - winter_melon_sales - okinawa_sales
    result = chocolate_sales
    return result

print(solution())