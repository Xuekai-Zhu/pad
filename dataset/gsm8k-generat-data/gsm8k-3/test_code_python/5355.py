def solution():
    """Lydia has 80 plants. 40% of her plants are flowering plants. Lydia wants to place a fourth of her flowering plants on the porch. If each flowering plant produces 5 flowers, how many flowers are there in total on the porch?"""
    # Compute the number of flowering plants Lydia has
    flowering_plants = 0.4 * 80

    # Compute the number of flowering plants Lydia wants to place on the porch
    porch_plants = flowering_plants / 4

    # Compute the total number of flowers on the porch
    porch_flowers = porch_plants * 5

    # Display the result
    result = porch_flowers
    return result

print(solution())