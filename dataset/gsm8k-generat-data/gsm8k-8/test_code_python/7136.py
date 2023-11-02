def solution():
    # Determine the total number of cookies
    total_cookies = 4 * 12 

    # Determine the total number of chocolate chips used
    total_chips = total_cookies * 7 

    # Determine the number of cookies eaten
    eaten_cookies = total_cookies / 2 

    # Determine the number of chips eaten
    eaten_chips = eaten_cookies * 7 

    # Determine the total number of chips left uneaten
    uneaten_chips = total_chips - eaten_chips 

    result = uneaten_chips
    return result

print(solution())