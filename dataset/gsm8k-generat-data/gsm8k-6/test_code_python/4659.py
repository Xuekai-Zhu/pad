def solution():
    # Calculate the number of women on the bus
    women = (2/3) * 48

    # Calculate the number of men on the bus
    men = 48 - women

    # Calculate the number of men standing
    standing_men = (1/8) * men

    # Calculate the number of men seated
    seated_men = men - standing_men

    result = seated_men
    return result

print(solution())