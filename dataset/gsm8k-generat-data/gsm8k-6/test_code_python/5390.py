def solution():
    # Calculate the number of cups sold for each flavor
    winter_melon = (2/5) * 50  # two-fifths of the sales are winter melon flavor
    Okinawa = (3/10) * 50  # three-tenths of the sales are Okinawa flavor
    chocolate = 50 - winter_melon - Okinawa  # the rest are chocolate-flavored milk tea

    result = chocolate
    return result

print(solution())