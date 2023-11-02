def solution():
    # Calculate the number of flowers on each plant
    plant1_flowers = 2
    plant2_flowers = 2 * plant1_flowers
    plant3_flowers = 4 * plant2_flowers

    # Calculate the total number of blossoms
    total_blossoms = plant1_flowers + plant2_flowers + plant3_flowers
    result = total_blossoms
    return result

print(solution())