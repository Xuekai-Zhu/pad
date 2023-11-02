def solution():
    """Nicole has 4 fish tanks. The first two tanks need 8 gallons of water each and the other two need 2 fewer gallons of water each than the first two tanks. If Nicole needs to change the water of the aquarium every week, how many gallons of water will she need in four weeks?"""
    first_tank_gallons = 8
    second_tank_gallons = 8
    third_tank_gallons = first_tank_gallons - 2
    fourth_tank_gallons = second_tank_gallons - 2
    total_gallons = (first_tank_gallons + second_tank_gallons + third_tank_gallons + fourth_tank_gallons) * 4
    result = total_gallons
    return result

print(solution())