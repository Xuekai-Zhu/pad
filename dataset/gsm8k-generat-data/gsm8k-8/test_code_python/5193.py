def solution():
    # Define the initial number of flowering and fruiting plants
    flowering_plants = 7
    fruiting_plants = 2 * flowering_plants

    # Add the new plants from the nursery
    flowering_plants += 3
    fruiting_plants += 2

    # Remove the plants given to Ronny
    flowering_plants -= 1
    fruiting_plants -= 4

    # Calculate the total number of remaining plants
    total_plants = flowering_plants + fruiting_plants
    result = total_plants
    return result

print(solution())