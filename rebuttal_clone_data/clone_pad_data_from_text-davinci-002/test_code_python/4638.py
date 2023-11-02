def solution():
    sonja_bread = 3
    sonja_coldcuts = 23
    barbara_soda = 5
    barbara_crackers = 4
    mario_rick_doodles = 6
    danica_plates = 4
    total_cost = sonja_bread + sonja_coldcuts + barbara_soda + barbara_crackers + mario_rick_doodles + danica_plates
    sonja_cost = sonja_bread + sonja_coldcuts
    result = sonja_cost - total_cost
    return result

print(solution())