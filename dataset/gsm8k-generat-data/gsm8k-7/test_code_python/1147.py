def solution():
    people_per_cubic_yard = 80
    city1_cubic_yards = 6400
    city2_cubic_yards = 9000

    # Calculate the number of people in city 1
    city1_people = people_per_cubic_yard * city1_cubic_yards

    # Calculate the number of people in city 2
    city2_people = people_per_cubic_yard * city2_cubic_yards

    # Calculate the difference in the number of people between the two cities
    diff_people = city2_people - city1_people
    result = diff_people
    return result

print(solution())