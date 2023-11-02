def solution():
    total_gallons = 65  # Jan collected 65 gallons of water
    car_cleaning_gallons = 7 * 2  # Jan uses 7 gallons of water to clean each of the two cars
    plant_watering_gallons = car_cleaning_gallons - 11  # Jan uses 11 fewer gallons to water plants than to clean cars
    remaining_gallons = total_gallons - car_cleaning_gallons - plant_watering_gallons  # Jan has this many gallons left after cleaning cars and watering plants
    plates_and_clothes_gallons = remaining_gallons / 2  # Jan uses half of the remaining gallons to wash plates and clothes

    result = plates_and_clothes_gallons
    return result

print(solution())