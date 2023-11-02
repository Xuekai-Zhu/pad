def solution():
    """Carol is an aviation engineer deciding how much fuel to put in a
    jet. The empty plane needs 20 gallons of fuel per mile. Each person
    on the plane increases this amount by 3 gallons per mile, and each
    bag increases it by 2 gallons per mile. If there are 30 passengers
    and 5 flight crew, and each person brought two bags, how many
    gallons of fuel does the plane need for a 400-mile trip?"""
    # Base fuel consumption
    base_fuel = 20

    # Fuel added per person and per bag
    fuel_per_person = 3
    fuel_per_bag = 2

    # Total passengers and bags
    passengers = 30
    crew = 5
    total_people = passengers + crew
    bags = total_people * 2

    # Total fuel consumption
    total_fuel = base_fuel + (fuel_per_person * total_people) + (fuel_per_bag * bags)
    fuel_for_400_mile_trip = total_fuel * 400

    result = fuel_for_400_mile_trip
    return result

print(solution())