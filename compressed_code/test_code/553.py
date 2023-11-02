def solution():
    
    
    base_fuel = 20

    
    fuel_per_person = 3
    fuel_per_bag = 2

    
    passengers = 30
    crew = 5
    total_people = passengers + crew
    bags = total_people * 2

    
    total_fuel = base_fuel + (fuel_per_person * total_people) + (fuel_per_bag * bags)
    fuel_for_400_mile_trip = total_fuel * 400

    result = fuel_for_400_mile_trip
    return result

print(solution())