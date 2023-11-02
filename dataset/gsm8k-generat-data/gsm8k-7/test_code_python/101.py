def solution():
    num_tubs = 6
    tubes_per_tub = 2
    num_people_per_tube = 3

    # Calculate the total number of tubes of lip gloss Marcy has
    total_tubes = num_tubs * tubes_per_tub

    # Calculate the total number of people Marcy can do makeup for
    total_people = total_tubes * num_people_per_tube
    result = total_people
    return result

print(solution())