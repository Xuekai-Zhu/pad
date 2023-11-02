def solution():
    
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