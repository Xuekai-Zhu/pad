def solution():
    """Julio has four bottles of orange soda and seven bottles of grape soda in his fridge. His friend Mateo has a bottle of orange soda and 3 bottles of grape soda in his fridge. If the amount of beverage in each bottle is 2 liters, how many more liters of soda does Julio have?"""
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