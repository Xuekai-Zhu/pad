def solution():
    jeremy_irons_played_drums_and_harmonica = True
    jeremy_irons_was_in_a_band_called_four_pillars_of_wisdom = True
    sweep_picking_is_a_guitar_playing_technique = True
    if jeremy_irons_played_drums_and_harmonica and jeremy_irons_was_in_a_band_called_four_pillars_of_wisdom and not sweep_picking_is_a_guitar_playing_technique:
        result = "no"
    else:
        result = "unknown"
    return result

print(solution())