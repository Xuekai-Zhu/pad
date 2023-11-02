def solution():
    
    first_tank_gallons = 8
    second_tank_gallons = 8
    third_tank_gallons = first_tank_gallons - 2
    fourth_tank_gallons = second_tank_gallons - 2
    total_gallons = (first_tank_gallons + second_tank_gallons + third_tank_gallons + fourth_tank_gallons) * 4
    result = total_gallons
    return result

print(solution())