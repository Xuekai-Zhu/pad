def solution():
    starting_clothes = 100
    donated_orphanage_1 = 5
    donated_orphanage_2 = donated_orphanage_1 * 3
    clothes_thrown_away = 15

    # Calculate the total number of clothes donated
    total_donated = donated_orphanage_1 + donated_orphanage_2

    # Calculate the total number of clothes remaining
    total_remaining_clothes = starting_clothes - total_donated - clothes_thrown_away
    result = total_remaining_clothes
    
    return result

print(solution())