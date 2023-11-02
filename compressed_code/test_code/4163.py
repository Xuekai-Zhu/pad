def solution():
    
    total_cups_sold = 50
    winter_melon_cups = (2 / 5) * total_cups_sold
    okinawa_cups = (3 / 10) * total_cups_sold
    chocolate_cups = total_cups_sold - winter_melon_cups - okinawa_cups
    result = chocolate_cups
    return result

print(solution())