def solution():
    total_cups = 50
    wintermelon_cups = (2/5) * total_cups
    okinawa_cups = (3/10) * total_cups

    # Calculate the number of chocolate-flavored milk tea cups
    chocolate_cups = total_cups - wintermelon_cups - okinawa_cups
    result = chocolate_cups
    return result

print(solution())