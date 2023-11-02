def solution():
    """Carol is an aviation engineer deciding how much fuel to put in a jet. The empty plane needs 20 gallons of fuel per mile. Each person on the plane increases this amount by 3 gallons per mile, and each bag increases it by 2 gallons per mile. If there are 30 passengers and 5 flight crew, and each person brought two bags, how many gallons of fuel does the plane need for a 400-mile trip?"""
    gallons_per_mile_empty = 20
    gallons_per_person_per_mile = 3
    gallons_per_bag_per_mile = 2
    total_passengers = 30
    total_crew = 5
    total_people = total_passengers + total_crew
    total_bags = total_people * 2
    total_gallons_per_mile = gallons_per_mile_empty + (gallons_per_person_per_mile * total_people) + (gallons_per_bag_per_mile * total_bags)
    total_gallons = total_gallons_per_mile * 400
    result = total_gallons
    return result

print(solution())