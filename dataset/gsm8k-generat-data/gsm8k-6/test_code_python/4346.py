def solution():
    # Calculate the total amount of soda in Julio's and Mateo's fridges
    julio_orange_soda = 4 * 2  # 4 bottles of orange soda with 2 liters each
    julio_grape_soda = 7 * 2  # 7 bottles of grape soda with 2 liters each
    mateo_orange_soda = 1 * 2  # 1 bottle of orange soda with 2 liters
    mateo_grape_soda = 3 * 2  # 3 bottles of grape soda with 2 liters each
    total_soda_julio = julio_orange_soda + julio_grape_soda
    total_soda_mateo = mateo_orange_soda + mateo_grape_soda
    difference = total_soda_julio - total_soda_mateo  # calculate the difference in liters
    result = difference
    return result

print(solution())