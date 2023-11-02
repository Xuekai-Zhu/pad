def solution():
    julio_orange_soda = 4
    julio_grape_soda = 7

    mateo_orange_soda = 1
    mateo_grape_soda = 3

    bottle_size = 2 # in liters

    # Calculate the total volume of orange soda that Julio has
    julio_orange_volume = julio_orange_soda * bottle_size

    # Calculate the total volume of grape soda that Julio has
    julio_grape_volume = julio_grape_soda * bottle_size

    # Calculate the total volume of orange soda that Mateo has
    mateo_orange_volume = mateo_orange_soda * bottle_size

    # Calculate the total volume of grape soda that Mateo has
    mateo_grape_volume = mateo_grape_soda * bottle_size

    # Calculate the total volume of soda that Julio has
    julio_total_volume = julio_orange_volume + julio_grape_volume

    # Calculate the total volume of soda that Mateo has
    mateo_total_volume = mateo_orange_volume + mateo_grape_volume

    # Calculate the difference in volume of soda that Julio has compared to Mateo
    difference = julio_total_volume - mateo_total_volume
    result = difference
    return result

print(solution())