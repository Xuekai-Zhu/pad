def solution():
    num_plants = 30

    # Calculate the number of plants left after the bugs ate 20 of them
    plants_left = num_plants - 20

    # Calculate the number of plants left after the bugs ate half of them
    plants_left /= 2

    # Calculate the number of plants left after the bugs ate 1 more
    plants_left -= 1
    result = plants_left
    return result

print(solution())