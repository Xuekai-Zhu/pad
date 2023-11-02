def solution():
    # Define variables
    total_potatoes = 300
    gina = 69
    tom = gina * 2
    anne = tom / 3

    # Calculate total number of potatoes given away
    given_away = gina + tom + anne

    # Calculate remaining potatoes
    remaining = total_potatoes - given_away
    result = remaining
    return result

print(solution())