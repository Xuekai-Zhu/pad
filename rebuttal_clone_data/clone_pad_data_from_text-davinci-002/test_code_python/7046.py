def solution():
     total_gallons = 65
     car_gallons = 7 * 2
     plant_gallons = (7 * 2) - 11
     remaining_gallons = total_gallons - car_gallons - plant_gallons
     washing_gallons = remaining_gallons / 2
     result = washing_gallons
     return result

print(solution())