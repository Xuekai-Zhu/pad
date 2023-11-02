def solution():
    current_plants = 20  # Mark currently has 20 strawberry plants
    months_since_planting = 3  # Mark has had the plants for 3 months

    # Calculate the number of plants Mark had before giving away 4
    current_plants_with_gift = current_plants + 4
    initial_plants = current_plants_with_gift / 2 ** months_since_planting
    result = initial_plants
    return result

print(solution())