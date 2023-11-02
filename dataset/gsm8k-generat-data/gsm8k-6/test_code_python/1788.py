def solution():
    # Calculate the number of lychees remaining
    lychees_sold = 500 / 2  # Mr. Shaefer sold half of the lychees
    remaining_lychees = 500 - lychees_sold  # Calculate the remaining number of lychees
    lychees_eaten = (3/5) * remaining_lychees  # Calculate the number of lychees that were eaten
    lychees_remaining = remaining_lychees - lychees_eaten  # Calculate the number of lychees that are remaining
    result = lychees_remaining
    return result

print(solution())