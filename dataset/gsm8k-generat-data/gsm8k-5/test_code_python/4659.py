def solution():
    total_passengers = 48  # There are 48 passengers on the bus

    # Calculate the number of women and men
    women = (2/3) * total_passengers
    men = total_passengers - women

    # Calculate the number of men standing
    men_standing = (1/8) * men

    # Calculate the number of men seated
    men_seated = men - men_standing
    result = men_seated
    return result

print(solution())