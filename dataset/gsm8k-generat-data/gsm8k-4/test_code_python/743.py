def solution():
    """Carol is an aviation engineer deciding how much fuel to put in a jet. The empty plane needs 20 gallons of fuel per mile. Each person on the plane increases this amount by 3 gallons per mile, and each bag increases it by 2 gallons per mile. If there are 30 passengers and 5 flight crew, and each person brought two bags, how many gallons of fuel does the plane need for a 400-mile trip?"""
    # Define the base fuel consumption rate
    base_rate = 20

    # Calculate the fuel consumption rate per person and per bag
    per_person_rate = 3
    per_bag_rate = 2

    # Calculate the total number of people and bags on the plane
    total_passengers = 30
    total_crew = 5
    total_people = total_passengers + total_crew
    total_bags = total_people * 2

    # Calculate the total fuel consumption rate
    total_rate = base_rate + (per_person_rate * total_people) + (per_bag_rate * total_bags)

    # Calculate the total fuel required for a 400-mile trip
    total_fuel = total_rate * 400

    result = total_fuel
    return result

print(solution())