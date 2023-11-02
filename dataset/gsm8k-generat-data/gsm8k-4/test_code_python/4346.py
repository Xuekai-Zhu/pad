def solution():
    """Julio has four bottles of orange soda and seven bottles of grape soda in his fridge. His friend Mateo has a bottle of orange soda and 3 bottles of grape soda in his fridge. If the amount of beverage in each bottle is 2 liters, how many more liters of soda does Julio have?"""
    # Define the number of bottles and liters of soda
    julio_orange_bottles = 4
    julio_grape_bottles = 7
    mateo_orange_bottles = 1
    mateo_grape_bottles = 3
    bottle_volume = 2 # liters

    # Calculate the total liters of soda for each person
    julio_total_liters = (julio_orange_bottles + julio_grape_bottles) * bottle_volume
    mateo_total_liters = (mateo_orange_bottles + mateo_grape_bottles) * bottle_volume

    # Calculate the difference in liters of soda
    difference = julio_total_liters - mateo_total_liters

    # Return the result
    result = difference
    return result

print(solution())