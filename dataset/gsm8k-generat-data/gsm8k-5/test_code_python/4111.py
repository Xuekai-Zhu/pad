def solution():
    total_apples = 23 + 37 + 14  # Total amount of apples on the shelves
    apples_sold = 36  # Amount of apples sold by noon

    # Calculate the mass of apples left on the shelves
    apples_left = total_apples - apples_sold
    result = apples_left
    return result

print(solution())