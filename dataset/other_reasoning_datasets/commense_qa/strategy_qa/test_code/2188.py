def solution():
    nintendo_release_year = 1983
    playstation_3_release_year = 2006
    nintendo_format = "cartridge"
    playstation_3_format = "CD"
    if nintendo_format == playstation_3_format and nintendo_release_year < playstation_3_release_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())