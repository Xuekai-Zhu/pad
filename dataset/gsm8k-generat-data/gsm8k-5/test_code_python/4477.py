def solution():
    brownies_per_batch = 20  # Melanie baked 20 brownies in each batch
    batches = 10  # Melanie baked 10 batches of brownies

    # Calculate the total number of brownies Melanie baked
    total_brownies = batches * brownies_per_batch

    # Calculate the number of brownies she set aside for the bake sale
    bake_sale_brownies = total_brownies * (3/4)

    # Calculate the number of brownies remaining after setting aside for the bake sale
    remaining_brownies = total_brownies - bake_sale_brownies

    # Calculate the number of brownies put in the container
    container_brownies = remaining_brownies * (3/5)

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies
    result = given_out_brownies
    return result

print(solution())