def solution():
    black_sea_volume = 547000
    moon_volume = 21900000000
    if moon_volume < black_sea_volume:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())