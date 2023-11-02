def solution():
    """Nicole has 4 fish tanks. The first two tanks need 8 gallons of water each and the other two need 2 fewer gallons of water each than the first two tanks. If Nicole needs to change the water of the aquarium every week, how many gallons of water will she need in four weeks?"""
    # Define the number of gallons of water needed for the first two tanks
    tank_1 = 8
    tank_2 = 8

    # Calculate the number of gallons of water needed for the other two tanks
    tank_3 = tank_1 - 2
    tank_4 = tank_2 - 2

    # Calculate the total number of gallons of water needed for each week
    total_gallons = tank_1 + tank_2 + tank_3 + tank_4

    # Calculate the number of gallons of water needed for four weeks
    total_gallons = total_gallons * 4

    # return the result
    result = total_gallons
    return result

print(solution())