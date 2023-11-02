def solution():
    # Calculate the total number of people
    total_people = 4

    # Calculate the total number of hours they will be on the road
    total_hours = 8 + 8

    # Calculate the total amount of water needed for each person for the entire trip
    water_per_person = (1/2) * total_hours

    # Calculate the total amount of water needed for the entire family for the entire trip
    total_water = water_per_person * total_people

    result = total_water
    return result

print(solution())