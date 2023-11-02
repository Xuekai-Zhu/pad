def solution():
    
    packs_per_carton = 5
    sticks_per_pack = 3
    cartons_per_box = 4
    boxes = 8
    total_sticks = packs_per_carton * sticks_per_pack * cartons_per_box * boxes
    result = total_sticks
    return result

print(solution())