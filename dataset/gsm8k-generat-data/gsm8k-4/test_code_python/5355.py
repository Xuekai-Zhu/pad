def solution():
    """Lydia has 80 plants. 40% of her plants are flowering plants. Lydia wants to place a fourth of her flowering plants on the porch. If each flowering plant produces 5 flowers, how many flowers are there in total on the porch?"""
    # Define the total number of plants and the percentage of flowering plants
    total_plants = 80
    flowering_percentage = 0.4

    # Calculate the number of flowering plants
    flowering_plants = total_plants * flowering_percentage

    # Calculate the number of flowering plants to be placed on the porch
    porch_plants = flowering_plants / 4

    # Calculate the total number of flowers on the porch
    porch_flowers = porch_plants * 5

    # return the result
    result = porch_flowers
    return result

print(solution())