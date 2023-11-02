def solution():
    total_plants = 30
    eaten_plants = 20
    remaining_plants = total_plants - eaten_plants

    # Calculate the number of plants left after the bugs ate half of the remaining plants
    remaining_plants = remaining_plants / 2

    # Calculate the number of plants left after the bugs ate 1 plant
    remaining_plants -= 1

    result = remaining_plants
    return result

print(solution())