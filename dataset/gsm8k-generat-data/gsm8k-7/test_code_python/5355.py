def solution():
    total_plants = 80
    flowering_plants_percent = 0.4
    porch_plants_percent = 0.25
    flowers_per_plant = 5

    # Calculate the total number of flowering plants
    total_flowering_plants = total_plants * flowering_plants_percent

    # Calculate the number of flowering plants to place on porch
    porch_flowering_plants = total_flowering_plants * porch_plants_percent

    # Calculate the total number of flowers on the porch
    total_flowers_on_porch = porch_flowering_plants * flowers_per_plant

    result = total_flowers_on_porch
    return result

print(solution())