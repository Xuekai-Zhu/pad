def solution():
    """Carol is an aviation engineer deciding how much fuel to put in a jet. The empty plane needs 20 gallons of fuel per mile. Each person on the plane increases this amount by 3 gallons per mile, and each bag increases it by 2 gallons per mile. If there are 30 passengers and 5 flight crew, and each person brought two bags, how many gallons of fuel does the plane need for a 400-mile trip?"""
    #Define the initial fuel requirement, per person and per bag requirement
    INITIAL_FUEL_PER_MILE = 20
    ADDITIONAL_PER_PERSON = 3
    ADDITIONAL_PER_BAG = 2

    # Define the number of passengers, crew and bags
    passengers = 30
    crew = 5
    bags = passengers * 2

    #Calculate the additional fuel needed per mile for passengers and bags
    per_person_fuel = passengers * ADDITIONAL_PER_PERSON
    per_bag_fuel = bags * ADDITIONAL_PER_BAG

    #Calculate the total fuel requirement for a 400-mile trip
    total_fuel = (INITIAL_FUEL_PER_MILE + per_person_fuel + per_bag_fuel) * 400

    #Display the total fuel requirement
    result = total_fuel
    return result

print(solution())