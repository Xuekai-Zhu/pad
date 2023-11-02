def solution():
    # Calculate the number of students in the marching band
    marching_band = 600 / 5

    # Calculate the number of students that play a brass instrument
    brass_players = marching_band / 2

    # Calculate the number of students that play the saxophone
    saxophone_players = brass_players / 5

    # Calculate the number of students that play the alto saxophone
    alto_sax_players = saxophone_players / 3

    result = alto_sax_players
    return result

print(solution())