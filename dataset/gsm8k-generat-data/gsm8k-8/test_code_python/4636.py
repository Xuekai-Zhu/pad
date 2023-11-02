def solution():
    # Define the initial number of biscuits Randy had
    randy_biscuits = 32

    # Add the number of biscuits given by his father and mother
    randy_biscuits += 13
    randy_biscuits += 15

    # Subtract the number of biscuits eaten by his brother
    randy_biscuits -= 20

    result = randy_biscuits
    return result

print(solution())