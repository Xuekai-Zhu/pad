def solution():
    cars = 3
    taxis = 6
    vans = 2
    people_per_car = 4
    people_per_taxi = 6
    people_per_van = 5

    # Calculate the total number of people who went on the hike
    total_people = (cars * people_per_car) + (taxis * people_per_taxi) + (vans * people_per_van)
    result = total_people
    return result

print(solution())