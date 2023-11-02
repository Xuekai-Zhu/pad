def solution():
    total_students = 600  # There are 600 students in the senior class
    marching_band_students = total_students / 5  # A fifth of the students are in the marching band
    brass_instrument_students = marching_band_students / 2  # Half of the marching band students play a brass instrument
    saxophone_players = brass_instrument_students / 5  # A fifth of the brass instrument players play the saxophone
    alto_sax_players = saxophone_players / 3  # A third of the saxophone players play the alto saxophone
    result = alto_sax_players
    return result

print(solution())