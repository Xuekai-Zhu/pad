def solution():
    # Calculate the difference in the number of people in two cities based on their cubic yards
    people_9000 = 9000 * 80  # number of people in a city with 9000 cubic yards
    people_6400 = 6400 * 80  # number of people in a city with 6400 cubic yards
    difference = people_9000 - people_6400  # difference in the number of people
    result = difference
    return result

print(solution())