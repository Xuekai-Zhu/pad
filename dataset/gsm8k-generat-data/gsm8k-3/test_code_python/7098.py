def solution():
    """Gertrude the chicken has 10 fleas.  The other chicken, Maud has 5 times the amount of fleas as Olive.  The final chicken, Olive has half the amount of flees as Gertrude.  How many fleas are there?"""
    # Define Gertrude's number of fleas
    gertrude_fleas = 10

    # Calculate Olive's number of fleas
    olive_fleas = gertrude_fleas / 2

    # Calculate Maud's number of fleas
    maud_fleas = olive_fleas * 5

    # Calculate the total number of fleas
    total_fleas = gertrude_fleas + olive_fleas + maud_fleas

    # Display the total number of fleas
    result = total_fleas
    return result

print(solution())