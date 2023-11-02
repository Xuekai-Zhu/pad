def solution():
    octavian_ships = 400
    octavian_infantry = 16000
    octavian_archers = 3000
    brazilian_navy_personnel = 80000
    brazilian_navy_marines = 16000
    brazilian_navy_torpedoes = True
    if brazilian_navy_personnel >= (octavian_infantry + octavian_archers) and brazilian_navy_torpedoes:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())