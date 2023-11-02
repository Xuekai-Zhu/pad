def solution():
    """Julio has four bottles of orange soda and seven bottles of grape soda in his fridge. His friend Mateo has a bottle of orange soda and 3 bottles of grape soda in his fridge. If the amount of beverage in each bottle is 2 liters, how many more liters of soda does Julio have?"""
    julio_orange = 4
    julio_grape = 7
    mateo_orange = 1
    mateo_grape = 3
    total_julio_soda = (julio_orange + julio_grape) * 2
    total_mateo_soda = (mateo_orange + mateo_grape) * 2
    difference = total_julio_soda - total_mateo_soda
    result = difference
    return result

print(solution())