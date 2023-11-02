def solution():
    """Nicole has 4 fish tanks. The first two tanks need 8 gallons of water each and the other two need 2 fewer gallons of water each than the first two tanks. If Nicole needs to change the water of the aquarium every week, how many gallons of water will she need in four weeks?"""
    # Define the amount of water needed for the first two tanks
    tank1_water = 8
    tank2_water = 8

    # Define the amount of water needed for the other two tanks
    tank3_water = tank1_water - 2
    tank4_water = tank2_water - 2

    # Calculate the total amount of water needed per week
    total_water = tank1_water + tank2_water + tank3_water + tank4_water

    # Calculate the total amount of water needed in four weeks
    total_water_4weeks = total_water * 4

    # Display the total amount of water needed in four weeks
    result = total_water_4weeks
    return result

print(solution())