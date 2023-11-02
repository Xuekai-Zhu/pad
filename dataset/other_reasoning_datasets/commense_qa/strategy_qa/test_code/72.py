def solution():
    kurt_cobain_genre = "Grunge rock"
    grunge_bands = ["Alice in Chains", "Pearl Jam", "Soundgarden"]
    latest_album_years = [2018, 2020]
    if kurt_cobain_genre in grunge_bands and max(latest_album_years) >= 1994:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())