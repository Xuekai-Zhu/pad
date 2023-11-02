def solution():
    pieces_of_clothing = 100
    donated_to_orphanage_1 = 5
    donated_to_orphanage_2 = donated_to_orphanage_1 * 3
    clothes_thrown_away = 15
    pieces_remaining = pieces_of_clothing - donated_to_orphanage_1 - donated_to_orphanage_2 - clothes_thrown_away
    result = pieces_remaining
    return result

print(solution())