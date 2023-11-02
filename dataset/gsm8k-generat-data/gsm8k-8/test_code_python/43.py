def solution():
    # Define the number of buildings that collapsed in the first earthquake
    first_earthquake = 4

    # Define the number of buildings that collapse in each subsequent earthquake
    collapsing_buildings = [first_earthquake]

    for i in range(3):
        # Double the number of collapsing buildings from the previous earthquake
        next_earthquake = collapsing_buildings[-1] * 2
        collapsing_buildings.append(next_earthquake)

    # Calculate the total number of buildings that collapsed
    total_collapses = sum(collapsing_buildings)

    result = total_collapses
    return result

print(solution())