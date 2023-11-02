def solution():
    sadie_speed = 3
    sadie_time = 2
    ariana_speed = 6
    ariana_time = 0.5
    sarah_speed = 4
    total_time = 4.5

    # Calculate the distance Sadie covered in the forest
    sadie_distance = sadie_speed * sadie_time

    # Calculate the distance Ariana covered in the open field
    ariana_distance = ariana_speed * ariana_time

    # Calculate the time Sarah spent running along the beach
    sarah_time = total_time - sadie_time - ariana_time

    # Calculate the distance Sarah covered along the beach
    sarah_distance = sarah_speed * sarah_time

    # Calculate the total distance of the race
    total_distance = sadie_distance + ariana_distance + sarah_distance
    result = total_distance
    return result

print(solution())