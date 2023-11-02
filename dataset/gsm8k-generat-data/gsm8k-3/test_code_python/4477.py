def solution():
    """Melanie baked 10 batches of brownies, with 20 brownies in each batch. She set aside 3/4 of the brownies in each batch for a bake sale, put 3/5 of the remaining in a container, and gave out the rest. How many brownies are given out?"""
    # Define the number of brownies in each batch
    BROWNIES_PER_BATCH = 20

    # Calculate the total number of brownies baked
    total_brownies = 10 * BROWNIES_PER_BATCH

    # Calculate the number of brownies set aside for the bake sale
    bake_sale_brownies = 3/4 * BROWNIES_PER_BATCH

    # Calculate the number of brownies remaining after the bake sale
    remaining_brownies = BROWNIES_PER_BATCH - bake_sale_brownies

    # Calculate the number of brownies put in a container
    container_brownies = 3/5 * remaining_brownies

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies

    # Display the number of brownies given out
    result = given_out_brownies
    return result

print(solution())