def solution():
    israeli_artists = ["Ofra Haza", "Idan Raichel", "Shye Ben Tzur"]
    hammerstein_ballroom_performers = ["David Bowie", "Radiohead", "LCD Soundsystem"]
    overlap = [artist for artist in israeli_artists if artist in hammerstein_ballroom_performers]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())