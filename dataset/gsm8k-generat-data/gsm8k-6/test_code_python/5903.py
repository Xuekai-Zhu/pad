def solution():
    teas_sold = 6  # given number of teas sold
    # Solve the equation 4(latte_sold) + 8 = total number of drinks sold
    # where latte_sold = number of lattes sold
    latte_sold = (8 + 4*teas_sold) / 4
    result = latte_sold
    return result

print(solution())