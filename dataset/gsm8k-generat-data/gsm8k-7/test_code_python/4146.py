def solution():
    num_seniors = 600
    marching_band_frac = 1 / 5
    brass_frac = 1 / 2
    sax_frac = 1 / 5
    alto_frac = 1 / 3

    # Calculate the number of students in the marching band
    num_marching_band = num_seniors * marching_band_frac

    # Calculate the number of students in the marching band who play a brass instrument
    num_brass_players = num_marching_band * brass_frac

    # Calculate the number of students in the marching band who play the saxophone
    num_sax_players = num_brass_players * sax_frac

    # Calculate the number of students in the marching band who play the alto saxophone
    num_alto_players = num_sax_players * alto_frac
    result = num_alto_players
    return result

print(solution())