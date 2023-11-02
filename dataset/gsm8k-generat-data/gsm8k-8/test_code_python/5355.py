def solution():
    # Calculate the number of flowering plants Lydia has
    flowering_plants = 0.4 * 80

    # Calculate the number of flowering plants Lydia wants on the porch
    plants_on_porch = 0.25 * flowering_plants

    # Calculate the total number of flowers on the porch
    flowers_on_porch = plants_on_porch * 5

    result = flowers_on_porch
    return result

print(solution())