def solution():
    # Calculate the total amount of orange soda Julio has
    julio_orange = 4 * 2

    # Calculate the total amount of grape soda Julio has
    julio_grape = 7 * 2

    # Calculate the total amount of orange soda Mateo has
    mateo_orange = 1 * 2

    # Calculate the total amount of grape soda Mateo has
    mateo_grape = 3 * 2

    # Calculate the total amount of soda Julio has
    julio_total = julio_orange + julio_grape

    # Calculate the total amount of soda Mateo has
    mateo_total = mateo_orange + mateo_grape

    # Calculate the difference in soda between Julio and Mateo
    difference = julio_total - mateo_total

    result = difference
    return result

print(solution())