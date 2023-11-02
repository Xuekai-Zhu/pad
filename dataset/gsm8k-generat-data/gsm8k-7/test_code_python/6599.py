def solution():
    total_potatoes = 300
    gina_potatoes = 69
    tom_potatoes = 2 * gina_potatoes
    anne_potatoes = tom_potatoes / 3

    # Calculate the total number of potatoes Johnson gave away
    given_potatoes = gina_potatoes + tom_potatoes + anne_potatoes

    # Calculate the number of potatoes Johnson has left
    potatoes_left = total_potatoes - given_potatoes
    result = potatoes_left
    return result

print(solution())