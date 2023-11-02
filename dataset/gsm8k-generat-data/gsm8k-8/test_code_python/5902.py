def solution():
    # Define the number of tomatoes produced by each plant
    plant1 = 2 * 12
    plant2 = (0.5 * plant1) + 5
    plant3 = plant2 + 2

    # Calculate the total number of tomatoes produced
    total_tomatoes = plant1 + plant2 + plant3
    result = total_tomatoes
    return result

print(solution())