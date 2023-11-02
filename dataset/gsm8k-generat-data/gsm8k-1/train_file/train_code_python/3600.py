def solution():
    """Nicole has 4 fish tanks. The first two tanks need 8 gallons of water each and the other two need 2 fewer gallons of water each than the first two tanks. If Nicole needs to change the water of the aquarium every week, how many gallons of water will she need in four weeks?"""
    tank_1_gallons = 8
    tank_2_gallons = 8
    tank_3_gallons = tank_1_gallons - 2
    tank_4_gallons = tank_2_gallons - 2
    total_gallons = (tank_1_gallons + tank_2_gallons + tank_3_gallons + tank_4_gallons) * 4
    result = total_gallons
    return result

print(solution())