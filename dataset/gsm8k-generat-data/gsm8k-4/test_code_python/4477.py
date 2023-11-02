def solution():
    """Melanie baked 10 batches of brownies, with 20 brownies in each batch. She set aside 3/4 of the brownies in each batch for a bake sale, put 3/5 of the remaining in a container, and gave out the rest. How many brownies are given out?"""
    # Define the number of batches and brownies per batch
    batches = 10
    brownies_per_batch = 20

    # Calculate the total number of brownies baked
    total_brownies = batches * brownies_per_batch

    # Calculate the number of brownies set aside for the bake sale
    bake_sale_brownies = total_brownies * 0.75

    # Calculate the remaining brownies
    remaining_brownies = total_brownies - bake_sale_brownies

    # Calculate the number of brownies put into a container
    container_brownies = remaining_brownies * (3/5)

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies

    # return the result
    result = given_out_brownies
    return result

print(solution())