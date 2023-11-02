def solution():
    cars = 2  # The swim team took 2 cars
    vans = 3  # The swim team took 3 vans
    people_per_car = 5  # Each car can hold 5 people
    people_per_van = 3  # Each van can hold 3 people
    max_people_per_car = 6  # Each car can hold a maximum of 6 people
    max_people_per_van = 8  # Each van can hold a maximum of 8 people

    # Calculate the total number of people the swim team brought
    total_people = (cars * people_per_car) + (vans * people_per_van)

    # Calculate the maximum number of people the swim team could have brought
    max_people = (cars * max_people_per_car) + (vans * max_people_per_van)

    # Calculate the difference between the maximum number of people and the actual number of people
    difference = max_people - total_people
    result = difference
    return result

print(solution())