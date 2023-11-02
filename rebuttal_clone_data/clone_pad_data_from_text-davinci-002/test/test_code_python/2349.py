def solution():
    total_students = 600
    band_students = total_students / 5
    brass_instrument_players = band_students / 2
    saxophone_players = brass_instrument_players / 5
    alto_saxophone_players = saxophone_players / 3
    result = alto_saxophone_players
    return result

print(solution())