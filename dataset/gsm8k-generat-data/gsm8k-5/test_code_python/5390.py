def solution():
    total_sales = 50  # The shop sold a total of 50 cups of milk tea
    winter_melon_sales = (2/5) * total_sales  # Two-fifths of the sales are winter melon flavor
    okinawa_sales = (3/10) * total_sales  # Three-tenths of the sales are Okinawa flavor
    chocolate_sales = total_sales - winter_melon_sales - okinawa_sales  # The rest are chocolate flavor

    result = chocolate_sales
    return result

print(solution())