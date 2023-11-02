def solution():
    
    julio_orange_soda = 4
    julio_grape_soda = 7
    mateo_orange_soda = 1
    mateo_grape_soda = 3
    liters_per_bottle = 2
    julio_total_liters = (julio_orange_soda + julio_grape_soda) * liters_per_bottle
    mateo_total_liters = (mateo_orange_soda + mateo_grape_soda) * liters_per_bottle
    difference = julio_total_liters - mateo_total_liters
    result = difference
    return result

print(solution())