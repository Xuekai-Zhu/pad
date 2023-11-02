def solution():
    # Define the initial number of napkins William had
    initial_napkins = 15

    # Define the number of napkins Olivia gave William
    olivia_napkins = 10

    # Define the number of napkins Amelia gave William
    amelia_napkins = 2 * olivia_napkins

    # Calculate the total number of napkins William now has
    total_napkins = initial_napkins + olivia_napkins + amelia_napkins
    result = total_napkins
    return result

print(solution())