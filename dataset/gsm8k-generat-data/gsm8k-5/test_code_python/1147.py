def solution():
    people_per_cubic_yard = 80  # Number of people living per cubic yard
    city1_volume = 6400  # Volume of first city in cubic yards
    city2_volume = 9000  # Volume of second city in cubic yards

    # Calculate the number of people in the first city
    city1_people = people_per_cubic_yard * city1_volume

    # Calculate the number of people in the second city
    city2_people = people_per_cubic_yard * city2_volume

    # Calculate the difference in population between the two cities
    difference = city2_people - city1_people
    result = difference
    return result

print(solution())