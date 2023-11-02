def solution():
    """Gertrude the chicken has 10 fleas. The other chicken, Maud has 5 times the amount of fleas as Olive. The final chicken, Olive has half the amount of flees as Gertrude. How many fleas are there?"""
    # Define the initial number of fleas on Gertrude
    gertrude_fleas = 10

    # Calculate the number of fleas on Olive
    olive_fleas = gertrude_fleas / 2

    # Calculate the number of fleas on Maud
    maud_fleas = olive_fleas * 5

    # Calculate the total number of fleas
    total_fleas = gertrude_fleas + olive_fleas + maud_fleas

    # Return the result
    result = total_fleas
    return result

print(solution())