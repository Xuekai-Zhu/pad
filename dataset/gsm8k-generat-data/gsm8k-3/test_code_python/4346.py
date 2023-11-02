def solution():
    """Julio has four bottles of orange soda and seven bottles of grape soda in his fridge. His friend Mateo has a bottle of orange soda and 3 bottles of grape soda in his fridge. If the amount of beverage in each bottle is 2 liters, how many more liters of soda does Julio have?"""
    # Define the number of bottles of each type of soda Julio has
    julio_orange = 4
    julio_grape = 7

    # Define the number of bottles of each type of soda Mateo has
    mateo_orange = 1
    mateo_grape = 3

    # Define the amount of beverage in each bottle
    bottle_size = 2

    # Calculate the total amount of orange soda Julio has
    total_orange = julio_orange * bottle_size

    # Calculate the total amount of grape soda Julio has
    total_grape = julio_grape * bottle_size

    # Calculate the total amount of orange soda Mateo has
    mateo_orange_total = mateo_orange * bottle_size

    # Calculate the total amount of grape soda Mateo has
    mateo_grape_total = mateo_grape * bottle_size

    # Calculate the total amount of soda Julio has
    total_julio = total_orange + total_grape

    # Calculate the total amount of soda Mateo has
    total_mateo = mateo_orange_total + mateo_grape_total

    # Calculate the difference in liters of soda between Julio and Mateo
    difference = total_julio - total_mateo

    # Display the difference in liters of soda
    result = difference
    return result

print(solution())