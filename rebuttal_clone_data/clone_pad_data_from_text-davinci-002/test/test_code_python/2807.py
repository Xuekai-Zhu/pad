def solution():
     cartons_packed = 50
     cans_per_carton = 20
     cartons_loaded = 40
     cans_left = cartons_packed * cans_per_carton - cartons_loaded * cans_per_carton
     result = cans_left
     return result

print(solution())