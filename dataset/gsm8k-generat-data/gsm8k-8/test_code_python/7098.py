def solution():
    # Define variables for the number of fleas on each chicken
    gertrude_fleas = 10
    olive_fleas = gertrude_fleas / 2
    maud_fleas = olive_fleas * 5

    # Calculate the total number of fleas
    total_fleas = gertrude_fleas + olive_fleas + maud_fleas
    result = total_fleas
    return result

print(solution())