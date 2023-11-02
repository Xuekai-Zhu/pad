def solution():
    # Calculate number of cups sold for winter melon and Okinawa flavors
    winter_melon_sales = (2/5) * 50
    okinawa_sales = (3/10) * 50

    # Calculate number of cups sold for chocolate flavor
    chocolate_sales = 50 - winter_melon_sales - okinawa_sales
    result = chocolate_sales
    return result

print(solution())