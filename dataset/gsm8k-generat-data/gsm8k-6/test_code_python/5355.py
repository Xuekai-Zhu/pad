def solution():
    # Calculate the number of flowering plants Lydia has
    num_flowering_plants = 0.4 * 80

    # Calculate the number of flowering plants she will place on the porch
    num_plants_on_porch = num_flowering_plants / 4

    # Calculate the total number of flowers on the porch
    total_flowers_on_porch = num_plants_on_porch * 5

    result = total_flowers_on_porch
    return result

print(solution())