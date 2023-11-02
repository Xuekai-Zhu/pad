def solution():
    sirius_constellation = "Canis Major"
    animal_constellations = ["Ursa Major", "Leo", "Scorpius", "Taurus", "Canis Minor", "Canes Venatici", "Aquarius", "Lyra"]
    if sirius_constellation in animal_constellations:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())