def solution():
    sony_ps4_units_sold = 108000000
    sega_saturn_units_sold = 9500000
    sony_playstation_units_sold = 102000000
    if sony_playstation_units_sold > sega_saturn_units_sold and sony_ps4_units_sold > 0:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())