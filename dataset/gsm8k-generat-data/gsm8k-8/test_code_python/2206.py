def solution():
    # Calculate the initial number of plants
    initial_plants = 6 + 2 + 4

    # Calculate the number of remaining plants after half of the tomato plants and one pepper plant died
    remaining_plants = (6/2) + (2) + (4-1)

    # Calculate the total number of vegetables harvested
    total_veggies = remaining_plants * 7
    result = total_veggies
    return result

print(solution())